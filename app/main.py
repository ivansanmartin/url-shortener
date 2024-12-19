from fastapi import FastAPI, Depends, status, HTTPException, Request
from app.api.v1.endpoints.url_shortener import router as url_shortener_router
from app.services.url_shortener import UrlShortenerService
from app.core.dependencies import get_url_shortener_service
from fastapi.responses import JSONResponse

app = FastAPI()
    
app.include_router(url_shortener_router, prefix="/api/v1")

@app.get("/{slug}", status_code=status.HTTP_200_OK)
async def get_shortener(slug: str, url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    response = url_shortener_service.get_shortener(slug)
    if not response.get("ok"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
    return response
