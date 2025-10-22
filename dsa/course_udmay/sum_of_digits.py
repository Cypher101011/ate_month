#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 19:43:16 2025

@author: a
"""

def sumOfDigit(n):
    assert n>=0 and int(n)==n,'the number has to be positive int'
    if n==0:
        return n
    else: 
        return int(n%10)+sumOfDigit(int(n/10))


print(sumOfDigit(10)) 