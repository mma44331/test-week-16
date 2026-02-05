from fastapi import FastAPI
import uvicorn
from routes import route
from json_to_mongo import create_db

app = FastAPI()

app.include_router(route)

@app.on_event("startup")
def create():
    create_db()



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000 , reload=True)
