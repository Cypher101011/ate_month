#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 20:22:24 2025

@author: ''"""

class Dog:
    def __init__(self,name,age):
        """ initiolize name and age attributes"""
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        '''simulate rolling over in respose to a command'''
        print(f'{self.name} rolled over ')

my_dog=Dog('willion',6)
print(f"my dog name is {my_dog.name} {my_dog.sit()}")