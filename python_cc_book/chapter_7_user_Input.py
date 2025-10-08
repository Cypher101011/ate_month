#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 10:43:12 2025

@author: a
"""

# even_or_odd.py
number =input("enter a number and I'll tell you if it's even odd: ")
number=int(number)

if number%2==0:
    print(f"{number} this number is even")
else:
    print("\n this number is odd")
    
    
# rental_car.py
car=input("enter what kind of car you want: ")

print(f"let me see i can find {car}")

# restaurantSeating.py
people=input("how many people are in their dinner group")

people=int(people)
if people>10:
    print("you have to wait")

else:
    print("your table is ready for {people} people")

# multiple_of_ten.py

if number%10==0:
    print('its multiple of ten')
else:
    print("its not")