from redis import Redis
from fastapi import HTTPException
import json
import os

class RedisCache:
    def __init__(self):
        self.redis_client = Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=int(os.getenv("REDIS_DB", 0)),
            decode_responses=True
        )

    def set_cache(self, key: str, value: dict, expiration: int = 3600):
        try:
            self.redis_client.set(key, json.dumps(value), ex=expiration)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error setting cache: {str(e)}")

    def get_cache(self, key: str):
        try:
            value = self.redis_client.get(key)
            return json.loads(value) if value else None
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting cache: {str(e)}")