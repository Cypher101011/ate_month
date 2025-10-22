#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 10:08:47 2025

@author: a
"""

def make_pizza(size=40,*toppings):
    print(f"\n making a {size}- inch pizza with following toppings:")
    for i in range(len(toppings)):
                   print(toppings[i])

make_pizza(50,'pepperoni')
make_pizza(40,'mushrooms','green peppers','extra cheese')

# user_profile.py
def build_profile(first,last,**user_info):
    '''build a dictonary containing everything we know
    about user'''
    user_info['first_name'] =first
    user_info['last_name'] =last
    return user_info

user_profile = build_profile('albert','einstein', 
                             location='princeton',
                             field ='physics')

for key,value in user_profile.items():
    print(key+' is ' +value)

# try it yourself 8.12

def sandwitches(*items):
    for i in range(len(items)):
        print(f' {i} you have order  sandwithche with {items[i]}')

sandwitches('nothing','chilli','garlig')

def build_profile(first,last,age,**user_info):
    '''build a dictonary containing everything we know
    about user'''
    user_info['first_name'] =first
    user_info['last_name'] =last
    user_info['age']=age
    return user_info

user_profile=build_profile('rohit', 'dandge',
                           23,location='borgaon',
                           field='tech')
print(user_profile)


def car_profile(manufacturer,model_name,**car_info):
    car_info['model']=model_name
    car_info['manufacturer']=manufacturer
    
    return car_info

new_car=car_profile('tesla','r2',
                    color='blue',
                    two_package=True)


print(f"\n\n\n \t\t______ \n\t \n\n{new_car}")