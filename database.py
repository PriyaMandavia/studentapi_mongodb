from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
stud_collection = db["stud"]
user_collection = db["user"]
