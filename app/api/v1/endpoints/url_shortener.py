from fastapi import APIRouter, Depends, status, Request, HTTPException
from app.services.url_shortener import UrlShortenerService
from app.core.dependencies import get_url_shortener_service
from app.models.url_shortener import UrlShortener
from api_key_manager_client import ApiKeyManagerClient

def validate_security_token(request: Request):
    api_key_manager = ApiKeyManagerClient('http://localhost:8000')
    
    api_key_entry: str = request.headers.get("X-API-Key")
    
    verification = api_key_manager.verify_api_key(api_key_entry)
    
    if not verification['ok']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=verification['message']
        )

router = APIRouter(dependencies=[Depends(validate_security_token)])


@router.get("/url-shorteners", status_code=status.HTTP_200_OK)
async def get_all_shorteners(url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    shorteners = url_shortener_service.get_shorteners()
    
    if not shorteners:
        return {"ok": False, "message": "No shorteners found"}
    
    return {"ok": True, "data": shorteners}

@router.post("/url-shortener", status_code=status.HTTP_201_CREATED)
async def create_shortener(
    shortener: UrlShortener, 
    url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    response = url_shortener_service.create_shortener(shortener.model_dump())
    return response
