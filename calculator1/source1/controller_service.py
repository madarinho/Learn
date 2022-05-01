from fastapi import FastAPI
from calculator1.source1.calculator import Calculator


calculator = Calculator()

calculate = FastAPI()

@calculate.get("/multiply/")
def multiply(x: float, y: float):
    return calculator.multiply(x, y)
