# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 22:05:22 2021

@author: enock_000
"""

# BMI calculator (For Adults)
#
stop = print("To stop program, enter 0 for both weight and height")
w = float(input("Enter your weight in kg\n>>> "))
h = float(input("Enter your height in m\n>>> "))
while w != 0 and h != 0:
    BMI = w/(h**2)
    if BMI < 18.5:
        BMI = round(BMI,1)
        print("BMI is", BMI)
        print("Underweight")
    elif BMI >= 18.5 and BMI < 25:
        BMI = round(BMI,1)
        print("BMI is", BMI)
        print("Normal")
    elif BMI >= 25 and BMI < 30:
        BMI = round(BMI,1)
        print("BMI is", BMI)
        print("Overweight")
    else:
        BMI = round(BMI,1)
        print("BMI is", BMI)
        print("Obese")
    w = float(input("Enter your weight in kg\n>>> "))
    h = float(input("Enter your height in m\n>>> "))

# Reference
# CDC. (2020). About adult BMI. 
# https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html