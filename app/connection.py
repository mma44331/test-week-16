import pymongo


def get_con_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mymongodb"]
    return db["employee_data_advanced"]

