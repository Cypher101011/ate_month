#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 11:37:32 2025

@author: a
"""

# linear scan .py1

def linear_search(array,item):
    i=0
    while i<len(array):
        if array[i]==item:
            return i
        i+=1
    return -1


    
linear_search('lucifer','f')

# Binary Search Algorithm

def binary_search(array,target):
        hight_index=len(array)
        low_index=0
    
        while low_index<=hight_index:
                index_mid=(hight_index+low_index)//2
            
                if array[index_mid]==target:
                    return index_mid
                if array[index_mid]<target:
                    low_index=index_mid+1 
                else:
                    hight_index=index_mid-1
        return -1

print(binary_search([1,2,3,4,4,5,6,7,12,32],4))