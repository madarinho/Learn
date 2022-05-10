import imp
from fastapi import FastAPI
from calculator1.source1.calculator import Calculator
from calculator1.source1.mongo_service import MongoSerivce


calculator = Calculator()
calculate = FastAPI()
mongo_service = MongoSerivce()


@calculate.get("/multiply/")
def multiply(x: float, y: float):
    mongo_service.insert(f'{x}*{y}')
    return calculator.multiply(x, y)

@calculate.get("/power/")
def power(x: float, y: float):
    mongo_service.insert(f'{x}**{y}')
    return calculator.power(x, y)

@calculate.get("/divide/")
def divide(x: float, y: float):
    mongo_service.insert(f'{x}/{y}')
    return calculator.divide(x, y)

@calculate.get("/find/")
def divide(number: float):
    return mongo_service.find_by_number(number)