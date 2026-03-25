from sqlalchemy.orm import Session
from app.models.car import CarModel
from app.schemas.car import CarCreate

def get_car(db: Session, car_id: int):
    query = db.query(CarModel).filter(CarModel.car_id == car_id)
    return query.first()

def get_all_cars(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(CarModel).offset(skip).limit(limit)
    return query.all()

def create_car(db: Session, car: CarCreate):
    db_car = CarModel(**car.model_dump())

    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    return db_car