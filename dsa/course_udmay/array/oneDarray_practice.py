#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:05:00 2025

@author: a
"""

from array import *

my_array=array('i',[1,23,4,5,543,4])
arr2=array('i',[1,3,46,45])
my_list=[1,10,1,1,1,1]

for i in my_array:
    print(i)
print(my_array[2])

print(my_array.append(12))
print(my_array)
my_array.insert(0,0)
print(my_array)

my_array.extend(arr2)
print(my_array)
my_array.fromlist(my_list)
print(my_array)

my_array.remove(23)
print(my_array)

my_array.pop()
print(my_array)

print(my_array.index(3))

my_array.reverse()
print(my_array)
print(reversed(my_array))

print(my_array.buffer_info())

print(my_array.count(1))
temp=my_array.tostring()
print(temp)
ints =array('i' )