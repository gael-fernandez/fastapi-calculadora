from fastapi import APIRouter
from app.models.operacion import numeros,FakeDB
router = APIRouter()
nuevos_numeros=FakeDB()
@router.post("/multiplicar")
def multiplicacion (datos:numeros):
    resultado = datos.a*datos.b
    return{
        "resultado":resultado
    }
@router.get("/sumar")
def suma(a:float,b:float):
    return {"resultado":a+b}
@router.put("/actualizar-config")
def actualizar(datos:numeros):
    nuevos_numeros.a=datos.a
    nuevos_numeros.b=datos.b
    return{"mensaje":"se actualizo con exito",
           "a":nuevos_numeros.a,
           "b":nuevos_numeros.b}
@router.delete("/reset")
def reset():
    nuevos_numeros.a=0
    nuevos_numeros.b=0
    return {"mensaje":"se receteo con exito",
            "a":nuevos_numeros.a,
            "b":nuevos_numeros.b}
