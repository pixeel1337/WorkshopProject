from pydantic import BaseModel, Field

class CustomerBase(BaseModel):
    customer_name: str = Field(..., min_length=3)
    customer_phone: str = Field(..., min_length=9, max_length=9)

    class Config:
        from_attributes = True

class CustomerCreate(CustomerBase):
    customer_id: int

class Customer(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True