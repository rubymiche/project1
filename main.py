from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# =====================================
# Exercise 7 - Mostrar claves
# =====================================
@app.get("/exercise7")
def exercise7():
    persona = {
        "nombre": "Ruby",
        "edad": 25,
        "ciudad": "Bogotá"
    }

    claves = list(persona.keys())

    return {
        "exercise": 7,
        "claves": claves
    }
