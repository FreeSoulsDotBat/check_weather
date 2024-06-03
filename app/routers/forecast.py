import requests
from fastapi import APIRouter

from app.config import settings
from app.db.database import forecast_collection, city_coordinate_collection

router = APIRouter()


@router.get("/forecast/{lat}&{lon}")
async def get_forecast(lat: float, lon: float):
    forecast = forecast_collection.find_one({"lat": round(lat, 4), "lon": round(lon, 4)}, {'_id': 0})
    if forecast is not None:
        return forecast
    else:
        response = requests.get(
            f"{settings.weather_base_url}lat={lat}&lon={lon}&units=metric&lang=pt_br&appid={settings.api_key}"
        )
        save_forecast_on_db(dict(response.json()))
        return response.json()


@router.get("/city_coordinates/{city}")
async def get_city_coordinates(city: str, limit: int = 1):
    city_coordinate = city_coordinate_collection.find_one({"name": city}, {'_id': 0})
    if city_coordinate is not None:
        return city
    else:
        response = requests.get(f"{settings.geocoding_base_url}q={city}&limit={limit}&appid={settings.api_key}")
        save_city_coordinate_on_db(dict(response.json()[0]))
        return response.json()


def save_forecast_on_db(forecast: dict):
    forecast_collection.insert_one(forecast)


def save_city_coordinate_on_db(city_info: dict):
    city_coordinate_collection.insert_one(city_info)
