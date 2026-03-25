from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CustomerModel(Base):
    __tablename__ = "customers"
    
    customer_id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_phone = Column(String, nullable=False)

    cars = relationship("CarModel", back_populates="owner")