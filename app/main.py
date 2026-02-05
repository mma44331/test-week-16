import json
from os import getenv

from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient

from routes import route
from json_to_mongo import create_db

app = FastAPI()

app.include_router(route)

@app.on_event("startup")
def create():
    mongo_uri = getenv("MONGO_URL", "mongodb://localhost:27017/")
    mongo_db = getenv("MONGO_DB", "mymongodb")
    mongo_collection = getenv("MONGO_COLLECTION", "employee_data_advanced")
    file_path = './employee_data_advanced.json'

    # Making Connection
    myclient = MongoClient(mongo_uri)

    # database
    db = myclient[mongo_db]

    # Created or Switched to collection
    # names: GeeksForGeeks
    Collection = db[mongo_collection]

    # Loading or Opening the json file
    with open(file_path) as file:
        file_data = json.load(file)

    # Inserting the loaded data in the Collection
    ins_result = Collection.insert_many(file_data)
    print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000 , reload=True)
