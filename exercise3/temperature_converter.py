# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: float) -> float:
   
    f = celsius * 9/5 + 32
    return round(f, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    
    c = (fahrenheit - 32) * 5/9
    return round(c, 2)


def celsius_to_kelvin(celsius: float) -> float:
    
    k = celsius + 273.15
    return round(k, 2)


def kelvin_to_celsius(kelvin: float) -> float:
    
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")

    c = kelvin - 273.15
    return round(c, 2)