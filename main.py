from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Session, engine, Base
from models.period import Period
import json

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/period/{id}")
def getPeriod(id: int):
    try:
        db = Session()
        academic_period = db.query(Period).filter(Period.id == id).first()
        db.close()
        return academic_period
    except:
        return {"message": "Period not found"}
    

@app.get("/periods")
def getPeriods():
    try:
        db = Session()
        academic_periods = db.query(Period).all()
        db.close()
        return academic_periods
    except:
        return {"message": "Periods not found"}

@app.post("/period")
def createPeriod(data: dict):
    try:
        db = Session()
        academic_period = Period(name=data["name"],year=data["year"], semester=data["semester"] , startDate=data["startDate"], endDate=data["endDate"])
        db.add(academic_period)
        db.commit()
        db.close()
        return {"message": "Period created successfully"}
    except:
        return {"message": "Period not created"}
    





