import os

import certifi
import pymongo.errors
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

ca = certifi.where()

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 800

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_db_client():
    if os.environ.get("ENVIRONMENT") == "development":
        app.mongodb_client = MongoClient('mongodb://mongoadmin:bdung@127.0.0.1:27017')
    else:
        app.mongodb_client = MongoClient(
            'mongodb+srv://cooking-db-admin:lh5zLcAz3HYIOwWD@cookingprocluster.jwyfoeq.mongodb.net/?retryWrites=true&w=majority',
            tlsCAFile=ca
        )


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get("/health")
def health():
    return {"status": "ok"}
