from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, Dict
from datetime import datetime

class UrlShortener(BaseModel):
    id: str = Field(..., description="Unique ID for the MongoDB document")
    original_url: str = Field(..., description="The original URL to be shortened")
    short_url: str = Field(..., description="The generated shortened URL")
    slug: str = Field(..., description="Unique identifier for the shortened URL")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Date and time the URL was created")
    updated_at: Optional[datetime] = Field(None, description="Date and time of the last update")
    clicks: int = Field(0, description="Number of times the shortened URL was clicked")
    expiration_date: Optional[datetime] = Field(None, description="Expiration date for the shortened URL")
    metadata: Optional[Dict[str, str]] = Field({}, description="Additional metadata such as IP address or user agent")
