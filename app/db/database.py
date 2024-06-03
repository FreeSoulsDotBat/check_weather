from pymongo import MongoClient

from app.config import settings

mongo_client = MongoClient(settings.mongo_db_url)
db = mongo_client[settings.mongo_db_name]

city_coordinate_collection = db["city_coordinate"]
forecast_collection = db["forecast"]
