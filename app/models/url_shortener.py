from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, Dict
from datetime import datetime

class UrlShortener(BaseModel):
    original_url: str = Field(..., description="The original URL to be shortened")