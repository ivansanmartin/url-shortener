from fastapi import APIRouter, Depends
from app.services.url_shortener import UrlShortenerService
from app.core.dependencies import get_url_shortener_service
from app.models.url_shortener import UrlShortener

router = APIRouter()

@router.get("/url-shortener")
async def get_urls(url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    shorteners = url_shortener_service.get_shortener()
    
    if not shorteners:
        return {"ok": False, "message": "No shorteners found"}
    
    return {"ok": True, "data": shorteners}

@router.post("/url-shortener")
async def create_shortener(
    shortener: UrlShortener, 
    url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    response = url_shortener_service.create_shortener(shortener.model_dump())
    return response
