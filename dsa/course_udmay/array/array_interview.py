#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:33:45 2025

@author: a
"""

# Question 1 find the missing number1
sn=0
def find_missing(arr):
    a=arr[0]
    d=arr[1]-arr[0]
    n=len(arr)+1
    sn=n/2*(2*a+(n-1)*d)
    return f"the missing element is {int(sn-sum(arr))}"

numbers_list = list(range(1, 101))
numbers_list.remove(11)
find_missing(numbers_list)

# Qestion 2 write a program to find all pairs of intergr whose usm is equal 
# gien number
pairs=[]
def pairs_sum(array,num):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j]+array[i]==num:
                if array[i]!=array[j]:
                    pairs.append([array[i],array[j]])

pairs_sum(numbers_list, 15)
print(pairs)

import numpy as np
myArray=np.array(numbers_list)
print(myArray)

# Question 4 find the maximum product of two interger from the arry
# whare all are positive
curent_product=0

def product(arr):
    curent_product=0
    for i in range(len(arr)):
        for j in  range(i+1,len(arr)):
           if i!=j:
               if curent_product < (arr[i]*arr[j]):
                   curent_product=arr[i]*arr[j]
                   indexes=[i,j]
    return f"{curent_product } and indexes are{indexes[0]}"
print(product(myArray))

# find unique
def find_is_uniq(arr):
    array=[]
    for i in range(len(arr)):
        if arr[i] not in array:
            array.append(arr[i])
        else:
            array.append(arr[i])

            print(f"duplicate found of element {arr[i]} at {i}  and  {array.index(arr[i])}")
            
find_is_uniq('luicifer')

def permuation(string1,string2):
    string1=map(string1)
    string2=map(string2)
    if len(string1)!=len(string2):
        return False
    string2=list(string2)
    for i in string1:
        if i in string2:
            string2.remove(i)
        else:
            return False
    return True
permuation('rlucfei', 'lucifer')

'''def permutation(string1,string2):
    return sorted(s1)==sorted(s2)'''
'''
from collection import counter
def permutation(s1,s2):
    return Sounter(s1)==Counter(s2)
'''
def permutation(a, b):
    if len(a) != len(b):
        return False
    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in b:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    for v in freq.values():
        if v != 0:
            return False
    return True


permutation('lucifermorningstar', 'lucifermorningstar')