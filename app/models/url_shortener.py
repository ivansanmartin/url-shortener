from pydantic import BaseModel, Field, UrlConstraints
from pydantic_core import Url
from typing_extensions import Annotated

class UrlShortener(BaseModel):
    original_url: Annotated[Url, UrlConstraints(allowed_schemes=["http", "https"])] = Field(..., description="The original URL to be shortened")