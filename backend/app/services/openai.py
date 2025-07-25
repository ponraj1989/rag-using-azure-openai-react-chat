from fastapi import HTTPException
import openai
import os

class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_response(self, query: str, context: str = "") -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-35-turbo",
                messages=[
                    {"role": "user", "content": query},
                    {"role": "system", "content": context}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))