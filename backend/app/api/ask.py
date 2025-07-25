from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from app.services import cognitive_search, openai, redis_cache

router = APIRouter()

class AskRequest(BaseModel):
    query: str
    model: Optional[str] = None
    location: Optional[str] = None

class AskResponse(BaseModel):
    answer: str
    context: List[dict]

@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    # Check cache first
    cached_response = redis_cache.get_cached_response(request.query, request.model, request.location)
    if cached_response:
        return cached_response

    # Perform vector search
    search_results = cognitive_search.search_documents(request.query, request.model, request.location)
    if not search_results:
        raise HTTPException(status_code=404, detail="No results found")

    # Generate answer using OpenAI
    answer = openai.generate_answer(request.query, search_results)

    # Prepare response
    response = AskResponse(answer=answer, context=search_results)
    
    # Cache the response
    redis_cache.cache_response(request.query, request.model, request.location, response)

    return response