from fastapi import FastAPI, Depends
from app.api.v1.endpoints.url_shortener import router as url_shortener_router
from app.services.url_shortener import UrlShortenerService
from app.core.dependencies import get_url_shortener_service

app = FastAPI()

app.include_router(url_shortener_router, prefix="/api/v1")

@app.get("/{slug}")
async def get_shortener(slug: str, url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    original_url = url_shortener_service.get_shortener(slug)
    return original_url
