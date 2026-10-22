

import math

num1 = math.sqrt(100)
print(f"num1: {num1}")

#%%

from math import sqrt
#from math import *

num2 = sqrt(81)
print(f"num2: {num2}")

#%%

import random as rng

print(rng.randint(10, 100))

#%%

import math

radius = 3
area = math.pi * radius ** 2

print(f"Area (r = {radius}): {area:.2f}")


distance = math.sqrt(3**2 + 4**2)
print(f"Distance: {distance}")

#%%

import random

names = [
        "Alice", "Bob", "Mark", "Sam"
    ]
picked = random.choice(names)
print(f"The lucky one: {picked}")

#%%

from datetime import date, timedelta

today = date.today()
due_date = today + timedelta(days=53999)

print(f"Due: {due_date}")

#%%

import json

student = {
        "name": "Sam",
        "score": 34
}

txt = json.dumps(student)
print(txt)

with open("output.json", "w") as fp:
    json.dump(txt, fp)
    











