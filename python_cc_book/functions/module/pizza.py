#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 10:16:39 2025

@author: a
"""


def make_pizza(size,*toppings):
    '''summarize the pizza we are about amek'''
    print(f'\n making a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'-{toppings}')
        
    return toppings