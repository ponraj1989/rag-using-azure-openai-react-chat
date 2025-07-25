from pydantic import BaseModel
from typing import Optional, List

class DocumentChunk(BaseModel):
    content: str
    embedding: List[float]
    metadata: dict

class SearchRequest(BaseModel):
    query: str
    filters: Optional[dict] = None

class SearchResponse(BaseModel):
    answer: str
    context: List[DocumentChunk]