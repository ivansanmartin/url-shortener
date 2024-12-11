from fastapi import APIRouter

router = APIRouter()

@router.get("/url-shortener")
async def get_urls():
    return {"ok": True}