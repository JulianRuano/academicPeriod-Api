from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["get"],
    allow_headers=["*"],
)

def load_academic_periods():
    with open("period.json", "r") as file:
        academic_periods = json.load(file)
    return academic_periods


@app.get("/period/{id}")
def getPeriod(id: int):
    academic_periods = load_academic_periods()
    for period in academic_periods:
        if period["id"] == id:
            return period
    return {"Error": "The academic period was not found"}

@app.get("/periods")
def getPeriods():
    academic_periods = load_academic_periods()
    return academic_periods

