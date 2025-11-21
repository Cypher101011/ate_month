#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:25:32 2025

@author: a
"""

from name_function import get_formatted_name

print("enter 'q' for quit any time")
while True:
    first=input("\n please give me a first name")
    if first =='q':
        break
    last=input("pleae give me a last name: ")
    if last == 'q':
        break
    
    formatted_name=get_formatted_name(first, last)
    print((f"neatly formatted name {formatted_name.title()}"))