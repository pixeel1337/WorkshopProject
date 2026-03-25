from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CarModel(Base):
    __tablename__ = "cars"

    car_id = Column(Integer, primary_key=True, index=True)
    nr_vin = Column(String, unique=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    owner_id = Column(Integer, ForeignKey("customers.customer_id"))

    owner = relationship("CustomerModel", back_populates="cars")