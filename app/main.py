from fastapi import FastAPI
from app.routers import calculadora
app = FastAPI()
app.include_router(calculadora.router,prefix="/calculadora")
