from sqlalchemy.orm import Session
from app.models.customer import CustomerModel
from app.schemas.customer import CustomerCreate


def get_customer(db: Session, customer_id: int):
    query = db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id)
    return query.first()

def get_all_customers(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(CustomerModel).offset(skip).limit(limit)
    return query.all()

def create_customer(db: Session, customer: CustomerCreate):
    db_customer = CustomerModel(**customer.model_dump())

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    

    return db_customer