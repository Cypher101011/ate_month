#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:14:58 2025

@author: a
"""

# Try it yourself
# 8.1Message
def display_message():
    print('hey everyone you are learning about  this chapter')

display_message()

def favorite_book(title):
    print(f'one of my favorite book is {title.title()}')
    
favorite_book('harry potter')

# pets.py
def describe_pet(animal_type,pet_name):
    '''display information about ap pet'''
    print(f'\n I have a {animal_type}')
    print(f"my {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'whillie')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# TRY IT YOURSELF
def make_shrit(size='large',text='I LOVE PYTHON'):
    print(f'shirt has size {size} and message is {text}')
    
make_shrit('large')


def describe_city(name,country):
    print(f'{name} is is {country}')

print(describe_city('rajastan', 'india'))
    