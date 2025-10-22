#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 11:29:34 2025

@author: a
"""

class Car:
    ''' a simple attempt to represent a cra'''
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer_reading")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
    def get_descriptive_name(self):330
        ''' return a neatly formatted description name'''
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name.title()0
my_new_car=Car('audi','a4',2024)
my_used_car=Car('subaru','outback',2009)
print(my_new_car.get_descriptive_name())00
