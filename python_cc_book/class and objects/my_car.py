#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 10:57:24 2025

@author: a
"""

from car import Car 
my_new_car=Car('audi','a5',3030)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=30
my_new_car.read_odometer()