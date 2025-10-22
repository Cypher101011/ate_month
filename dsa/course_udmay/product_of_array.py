#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 20:33:48 2025

@author: a
"""

def product_of_array(array):
    if 0 in array:
        return 0
    if array==[]:
        return 1
    else:
        return array[-1]*product_of_array(array[0:len(array)-1])
        
product_of_array([1,2,5,6,23])

def productOfArray(array):
    product=1
    if 0 in array:
        return 0
    if array==[]:
        return 1 
    for i in range(len(array)):
        product*=array[i]
    return product

        
productOfArray([1,2,3,2,2])
        