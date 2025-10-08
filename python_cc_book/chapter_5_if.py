#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:58:52 2025

@author: a
"""

# cars.py
cars=['audi','bmw','subaru','marcedese','toyota']

for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())
        
# toppings.py

requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("hold the anchovies")
    
requested_toppings=['mushrooms','onions','pineapple']

print('mushooms' in requested_toppings)

# banned_users.py 
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(f'{user.title()}.you can post a response if you whish')
    
# try it yourself

# age=int(input("enter your age: "))

# if age<4:
#     print("your admission cost is free")
# elif age<18:
#     print("your cost is 20 $")
# else:
#     print("you have to py 40$ to inter")
    
# if age<4:
#     price=0
# elif age<18:
#     price=20
# else:
#     price=40

# print(f'your admission cost is ${price}')

# alien_color=['green','yellow','red']
# if alien_color=='green':
#     print('you got 5')

# if alien_color=

age=int(input(('enter your age')))
if age < 2:
    print('you are baby')
elif age>=2 and age <4:
    print('you are toddler')
elif age >=4 and age <13:
    print('you are just kid')
elif age >=13 and age>20:
    print('teenager')
elif age >20 and age <=65:
    print("you are adult")
elif age>65:
    print("you are elder")
    
    
favourate_food=['pizza','icecream','burger','chocklet']

food =input('inter food item you want : ')

if food in favourate_food:
    print(f'{food} is present and you really like {food}')
