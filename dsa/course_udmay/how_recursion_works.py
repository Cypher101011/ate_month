#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 21:28:34 2025

@author: a
"""

def firstMethod():
    secondMethod()
    print("i am first method")

def secondMethod():
    thirdMethod()
    print("i am second method")

def thirdMethod():
    fourtMethod()
    print("i am the third method")
    
def fourtMethod():
    # firstMethod()
    print('i am foruth method')

firstMethod()

#how recursion works ?
def recursiveMethod(n):
    if n<1:
        print('n is less than 1')
    else:
        recursiveMethod((n-1))
        print(n)
        
recursiveMethod(8)