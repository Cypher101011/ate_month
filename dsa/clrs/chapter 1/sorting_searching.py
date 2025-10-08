#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 10:26:22 2025

@author: a
"""
array=[12.3,3,4,5,3]

def sum_array(a):
        sum =0
        for i in range(len(a)):
            sum +=a[i]
            # print(sum)
        return sum

print(sum_array([12.3,3,4,5,3]))

# rewrite the insertion osort procecure to sort into monotonically decreasing 
# insted of monotonically increasing

def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        
        while j>=0 and a[j]<key:
            a[j+1]=a[j]
            j-=1
            
        a[j+1]=key
    return a
    
print(insertion_sort([12.3,3,4,5,3]))
            
            
             