from pydantic import BaseModel, Field

class CarBase(BaseModel):
    nr_vin: str = Field(..., min_length=17, max_length=17)
    brand: str = Field(..., min_length=1)
    model: str = Field(..., min_length=1)
    year: int = Field(..., ge=1990)

class CarCreate(CarBase):
    owner_id: int

class Car(CarBase):
    car_id: int
    owner_id: int

    class Config:
        from_attributes = True