#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 09:42:13 2025

@author: a
"""

# greet_users.py 
def greet_users(names):
    '''print a simple greeting'''
    for name in names:
        msg=f'Hello,{name.title()}'
        print(msg)
        
usernames=['hanhan','ty','margot']
greet_users(usernames)

# printing_models.py
# start with some design theat need to be printed
unprinted_desings=['phone case','robot pendant','dedechahedron']
completed_models=[]

# simululate printing each desing,until none are left
# move each desing to completed models after printitn
while unprinted_desings:
    current_desing=unprinted_desings.pop()
    print(f'printing model:{current_desing}')
    completed_models.append(current_desing)
    
# display all completed models33

# modification
def print_models(unprinted_desings,completed_models):
    '''simulate printiting each design,until none are left
    move each desing to completed_modelse after printitng.'''
    while unprinted_desings:
        current_desing=unprinted_desings.pop()
        print(f"printing model: {current_desing}")
        completed_models.append(current_desing)
def show_completed_models(completed_models):
    '''show all modelse theat were printed"'''
    print("\n the following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_desings=['phone case','robot pendant','dedecahedron']
completed_models=[]
print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)   
print(completed_models)
print(unprinted_desings)














 