from fastapi import FastAPI
from .database import engine, Base
from .routers import customers, cars

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="System obsługi warsztatu samochodowego",
    description="API do zarzadzania klientami i ich pojazdami",
    version="1.0.0"
)

app.include_router(customers.router)
app.include_router(cars.router)

@app.get("/")
def home():
    return {"status": "Server running"}