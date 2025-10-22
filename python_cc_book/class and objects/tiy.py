#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 11:35:39 2025

@author: a
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is a 5-star restaurant whose name is {self.restaurant_name} "
              f"\nand has cuisine {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open!")

# Create objects
restaurant = Restaurant('Lux', 'Bar')
restaurant1 = Restaurant('3Str', '3Star')
restaurant3 = Restaurant('Hell Kitchen', 'Devil Tear')

# Call methods
restaurant.describe_restaurant()
restaurant1.describe_restaurant()
restaurant3.describe_restaurant()

# Open one restaurant
restaurant.open_restaurant()




Restaurant.number_served=0
def set_number_served(self,number):
    self.number_served=number
Restaurant.set_number_served=set_number_served
new_restorant=Restaurant('lux','bar')
r2 =Restaurant('hells kitchen', 'devils tear')
new_restorant.set_number_served(11)
print(new_restorant.number_served )
