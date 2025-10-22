#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 10:10:23 2025

@author: a
"""

a=[1,2,3,4,5,6]
b=[5,6,7,8]

print(a+b)

print(a*2)

print(f"length {len(a)}")

print(max(a ))
array=[]
# while (True):
#     inp=input('enter numbers')
#     if inp=='done': break
#     value =float(inp)
#     array.append(value)

# print(f"average is {sum(array)/len(array)}")

lIst='lucifer_morningstar the_divil'

b=lIst.split(' ')
print(b)
b=' '.join(b)
print(b)
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
# a[::2]=10#,20,30,40,50,60
print(a)
print(a[3:0:-1])
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])


data = [
        [[1, 2], [3, 4]], 
        [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))