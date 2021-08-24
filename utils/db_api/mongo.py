from pymongo import MongoClient
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from data.config import IP

client = MongoClient(IP)
storage = MongoStorage()

database = client["breille"]

users_db = database["users"]
profiles_db = database["profiles"]