#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:57:34 2025

@author: a
"""
try:
    print(0/0)
except ZeroDivisionError:
    print("you can't divide by zero")

print("give me two numbers,  and i'll divide them")
print("enter q for quit")
while True:
    first_number=input("\nfirst number: ")
    if first_number=='q':
        break
    second_number=input("second Number: ")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:print("you cannot divide by zero")
        
    print(answer)