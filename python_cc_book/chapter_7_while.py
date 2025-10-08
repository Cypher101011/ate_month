#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 11:03:33 2025

@author: a
"""
# counting.py1
current_number=1 
while current_number<=5:
    print(current_number)
    current_number+=1
    
# parrot.py1
prompt='tell me something and i will repeat it back to you'
prompt+='\n enter "q" to end the program'
message=""
while message!='q':
    message=input(prompt)
    print(message)