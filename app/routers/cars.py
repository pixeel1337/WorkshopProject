from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import car as car_crud
from app.crud import customer as customer_crud
from app.schemas import car as car_schema
from app.database import get_db

router = APIRouter(
    prefix="/cars",
    tags=["samochody"]
)

############################################################
# Dodac sprawdzanie czy wlascicel istnieje
############################################################


@router.post("/", response_model=car_schema.Car)
def create_car(car: car_schema.CarCreate, db: Session = Depends(get_db)):
    return car_crud.create_car(db=db, car=car)

@router.get("/", response_model=list[car_schema.Car])
def get_all_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return car_crud.get_all_cars(db, skip=skip, limit=limit)

@router.get("/{car_id}", response_model=car_schema.Car)
def get_car(customer_id: int, db: Session = Depends(get_db)):
    return car_crud.get_car(db=db, customer_id=customer_id)

