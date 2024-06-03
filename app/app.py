from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from app.routers import forecast


def create_app() -> FastAPI:
    app = FastAPI(title="Check Weather API")

    app.include_router(forecast.router)

    # For local development
    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Generic health route to sanity check the API
    @app.get("/")
    async def health():
        return {
            "api_key": settings.api_key,
            "weather_base_url": settings.weather_base_url,
            "geocoding_base_url": settings.geocoding_base_url
        }

    return app
