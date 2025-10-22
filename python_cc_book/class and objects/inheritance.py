#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 11:14:02 2025

@author: a
"""

# electric_car.py 
class Car:
    ''' a simple attempt to represent a car'''
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def fill_gas_tank(self):
        print("fill the gas tank")
    def get_descriptive_name(self):
        '''return a newatly formatted descriptive name'''
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        '''print a statement showing the car's mileage'''
        print(f'this car has {self.odometer_reading} miles on it')
    def update_odometer(self,mileage):
        '''set the odometer reading to the given value'''
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")
    def increment_odometer(self,miles):
        '''add the given amount to the odometer reading.'''
        self.odometer_reading+=miles
class Battery:
    def __init__(self,battery_size=40):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"this car has a {self.battery_size} -kWh battery")
    def get_range(self):
        if self.battery_size==40:range=150
        elif self.battery_size==65:range=225
        print(f"this car can go about {range} miles on a full charge.")
    
class Electric_car(Car):
    '''represent aspect of a car, specific to electric vehicles'''
    def __init__(self,make,model,year):
        '''initilize  attributes of the parent class.'''
        super().__init__(make,model,year)
        self.battery=Battery()
    def fill_gas_tank(self):
        print("electric car doe't have a gs tank to fill")
   


my_leaf=Electric_car('nissan', 'leaf', 2024)
my_leaf.battery.describe_battery()
print(my_leaf.get_descriptive_name())   
my_leaf.battery.get_range()  