#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 11:09:21 2025

@author: a
"""

def get_formatted_name(first_name,last_name):
    '''return a full name, neatly formatted/'''
    full_name=f'{first_name} {last_name}'
    return full_name.title()

musician=get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name2(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f'{first_name} {middle_name} {last_name}'
    else:
        full_name=f'{first_name} {last_name}'
    return full_name.title()

musician=get_formatted_name2('lucifer', 'morningstar')
print(musician)

musician=get_formatted_name2('rohit','dandge','raju')
print(musician)

# returning a dictornayr
def build_person(first_name,last_name):
    person={'fist':first_name,'last':last_name}
    return person
musician=build_person('jimi', 'hendrix')

print(musician.items())

def build_person2(first_name,last_name,age=None):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person

musician=build_person2('jimmy', 'hendrix',age=27)
print(musician)
        
while True:
    print('please tell me your name:')
    print("enter 'q' for quit")
    
    f_name=input("first name: ")
    if 'q' == f_name:
        break
    l_name=input('last name: ')
    if 'q'==  l_name:
        break
    
    formatted_name=get_formatted_name(f_name,l_name)
    print(f'\n Hello, {formatted_name}')