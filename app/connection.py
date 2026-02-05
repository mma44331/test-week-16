import pymongo
import os


def get_con_db():
    client = pymongo.MongoClient(os.getenv("MONGO_URL","mongodb://localhost:27017/"))
    db = client["mymongodb"]
    return db["employee_data_advanced"]

