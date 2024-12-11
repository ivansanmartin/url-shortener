from fastapi import FastAPI
from app.api.v1.endpoints.url_shortener import router as url_shortener_router

app = FastAPI()

app.include_router(url_shortener_router, prefix="/api/v1")

@app.get("/")
def home():
    return {"hello": "world"} 