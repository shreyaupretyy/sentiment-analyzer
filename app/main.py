import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.sentiment import router as sentiment_router
from app.core.config import get_settings

# Configure logging
logging.basicConfig(
    level=get_settings().log_level.upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Initialize FastAPI application
app = FastAPI(
    title=get_settings().app_name,
    version=get_settings().app_version,
    description="A sentiment analysis microservice built with FastAPI",
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(sentiment_router, prefix="/api/v1", tags=["sentiment"])


@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=get_settings().host,
        port=get_settings().port,
        reload=get_settings().environment == "development",
    )