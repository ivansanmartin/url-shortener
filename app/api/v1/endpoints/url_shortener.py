from fastapi import APIRouter, Depends
from app.services.url_shortener import UrlShortenerService
from app.core.dependencies import get_url_shortener_service

router = APIRouter()

@router.get("/url-shortener")
async def get_urls(url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    shorteners = url_shortener_service.get_shortener()
    
    if not shorteners:
        return {"ok": False, "message": "No shorteners found"}
    
    return {"ok": True, "data": shorteners}
