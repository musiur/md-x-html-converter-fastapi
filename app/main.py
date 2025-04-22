from fastapi import FastAPI
from .routers import all_routers as routers

app = FastAPI(
    title="MarkItDown API",
    description="API for MarkItDown application",
    version="0.1.0"
)

# Include routers
for router in routers:
    app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to MarkItDown. Use /api for API endpoints."}