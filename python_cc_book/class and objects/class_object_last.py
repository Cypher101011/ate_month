#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 11:02:37 2025

@author: a
"""
# modifying attribut valuses
# there is possible three wats
'''
1 change didrctly at instance
2 set value through method 
3 increment value (add certaim amount to it through metheod)

# 1 modyfying an attribute's value dirctly'''

class Car:
    
    def __init__(self,make,model,year):
        
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        
            pass
    def read_odometer(self):
            print(f'this car has {self.odometer_reading} miles on it')
# ---- Create object ----
my_new_car = Car('audi', 'a5', 2025)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# ---- Modify attribute directly ----
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# ---- Define methods outside class ----
def update_odometer(self, mileage):
    """Set the odometer reading to the given value; reject rollback"""
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")


def increment_odometer(self, miles):
    """Add given amount to the odometer reading"""
    if miles < 0:
        print("You can't roll back miles!")
    else:
        self.odometer_reading += miles


# ---- Attach them to class ----
Car.update_odometer = update_odometer
Car.increment_odometer = increment_odometer


# ---- Test ----
my_new_car.update_odometer(22)
my_new_car.read_odometer()

my_used_car = Car('bugatti', 'chiron', 2020)
my_used_car.update_odometer(24_134)
my_used_car.read_odometer()

my_used_car.increment_odometer(199)
my_used_car.read_odometer()
