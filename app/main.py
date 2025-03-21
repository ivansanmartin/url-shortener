from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints.url_shortener import router as url_shortener_router
from app.services.url_shortener import UrlShortenerService
from app.core.dependencies import get_url_shortener_service

app = FastAPI()

origins = [
    "https://ivsm.link",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(url_shortener_router, prefix="/api/v1")

@app.get("/{slug}", status_code=status.HTTP_200_OK)
async def get_shortener(slug: str, url_shortener_service: UrlShortenerService = Depends(get_url_shortener_service)):
    response = url_shortener_service.get_shortener(slug)
    if not response.get("ok"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response)
    return RedirectResponse(response["original_url"], status_code=307)
