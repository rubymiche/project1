from fastapi import FastAPI

app = FastAPI(
	title="API de Programación Agéntica - EPII Diurno",
    description="Elaborado por Ruby  michel coello guzman ",
    version="1.0.0",
    contact={
        "name": "Ruby coello ",
        "email": "coelloruby9@gmail.com",
    })

# Datos personales
persona = {
    "nombre": "Ruby coello",
    "edad": 21,
    "ciudad": "Barranquilla"
}


# Exercise 1 - Mostrar nombre
@app.get("/exercise1")
def exercise1():
    return {
        "exercise": 1,
        "resultado": persona["nombre"]
    }


# Exercise 2 - Sumar dos números fijos
@app.get("/exercise2")
def exercise2():
    a = 10
    b = 5
    return {
        "exercise": 2,
        "numero1": a,
        "numero2": b,
        "resultado": a + b
    }


# Exercise 3 - Validar número par fijo
@app.get("/exercise3")
def exercise3():
    numero = 20
    return {
        "exercise": 3,
        "numero": numero,
        "resultado": "Es par" if numero % 2 == 0 else "Es impar"
    }


# Exercise 4 - Recorrer lista
@app.get("/exercise4")
def exercise4():
    lista = [1, 2, 3, 4, 5]
    return {
        "exercise": 4,
        "lista_recorrida": lista
    }


# Función multiplicar
def multiplicar(x: int, y: int):
    return x * y


# Exercise 5 - Multiplicación fija
@app.get("/exercise5")
def exercise5():
    a = 4
    b = 6
    return {
        "exercise": 5,
        "numero1": a,
        "numero2": b,
        "resultado": multiplicar(a, b)
    }


# Exercise 6 - Mostrar persona
@app.get("/exercise6")
def exercise6():
    return {
        "exercise": 6,
        "persona": persona
    }


# Exercise 7 - Mostrar claves del diccionario
@app.get("/exercise7")
def exercise7():
    return {
        "exercise": 7,
        "claves": list(persona.keys())
    }

# Exercise 8 - Clase Producto
@app.get("/exercise8")
def exercise8():
    class Producto:
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

    p = Producto("Laptop", 2500)

    return {
        "exercise": 8,
        "producto": {
            "nombre": p.nombre,
            "precio": p.precio
        }
    }


# Exercise 9 - Try / Except
@app.get("/exercise9")
def exercise9():
    try:
        numero = int("abc")
        resultado = numero
    except:
        resultado = "Error al convertir a número"

    return {
        "exercise": 9,
        "resultado": resultado
    }


# Exercise 10 - Lista del 1 al 10
@app.get("/exercise10")
def exercise10():
    numeros = list(range(1, 11))

    return {
        "exercise": 10,
        "lista": numeros
    }


# Exercise 11 - Duplicar lista
@app.get("/exercise11")
def exercise11():
    lista = [1, 2, 3, 4, 5]
    duplicada = [x * 2 for x in lista]

    return {
        "exercise": 11,
        "original": lista,
        "duplicada": duplicada
    }


# Exercise 12 - Mayor de dos números
@app.get("/exercise12")
def exercise12():
    a = 10
    b = 20

    mayor = a if a > b else b

    return {
        "exercise": 12,
        "numero1": a,
        "numero2": b,
        "mayor": mayor
    }


# Exercise 13 - Leer archivo
@app.get("/exercise13")
def exercise13():
    with open("data.txt", "r") as f:
        contenido = f.read()

    return {
        "exercise": 13,
        "contenido": contenido
    }


# Exercise 14 - Diccionario a JSON
@app.get("/exercise14")
def exercise14():
    import json

    persona = {
        "nombre": "Maria",
        "edad": 20
    }

    json_data = json.dumps(persona)

    return {
        "exercise": 14,
        "diccionario": persona,
        "json": json_data
    }

