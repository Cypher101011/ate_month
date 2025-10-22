#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 20:20:20 2025

@author: a
"""

def factorial(num1):
    assert num1<0 or int(num1)!=0,'you cant use negative or fraction'
    if num1 in [1,0,2]:
        return num1
    else:
        return num1*factorial(num1-1)
factorial(5)


def fact_it(num1):
    fact=1
    assert num1<0 or int(num1)!=0,'you cant use negative or fraction'
    if num1 in [0,1,2]:
        return num1
    else:
        for i in range(1,num1+1):
            fact*=i
    return fact
            
fact_it(4)
