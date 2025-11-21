#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 16:47:42 2025

@author: a

"""
from pathlib import Path
# 10.6 addition
# while True:
    
#     try:
#         a =int(input("enter two numbers to add"))
#         b=int(input())
#         if a or b == 'q':
#             exit
        
#         print(a+b)
#     except ValueError:
#         print("input must be numbers")
dog=0
filenames=['cat.txt',
           'dog.txt','animal.txt','r_j.txt']
for filename in filenames:
    try:
        path=Path(filename)
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"sorry, the file {path} not exist")
    else:
       dog=contents.lower().count(' torcher ')
       print(dog)