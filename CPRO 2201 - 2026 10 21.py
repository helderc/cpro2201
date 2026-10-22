
import calculator

print(f"add: {calculator.add(2, 3)}")


#%%

#from calculator import *
import calculator
#from math import *
import math

print(f"subtract: {calculator.subtract(5, 2)}")
math.subtract(1,2)

#%%

from mathop import subtraction
#from stringop import 

print(subtraction.subtract(6, 1))


#%%

from datetime import date, datetime

today_str = "2026-10-21"
date_now = datetime.strptime(today_str, "%Y-%m-%d").date()
print(date_now)

print(date.today() == date_now)








