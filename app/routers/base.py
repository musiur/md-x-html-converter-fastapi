from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["base"]
)

@router.get("/")
async def root():
    return {"message": "Welcome to MarkItDown API"}