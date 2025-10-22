#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 11:30:02 2025

@author: a
"""

import numpy as np 
twoDarray=np.array([[11,15,19,5],
                    [10,14,11,5],
                    [12,17,12,8],
                    [15,18,14,9]])

print(twoDarray)
for i in range(len(twoDarray[1])):
    for j in range(len(twoDarray[1])):           
                   print(twoDarray[i][j],end=' ')
    print('\n')

newArray=twoDarray
newArray=np.insert(twoDarray,2,[[1,2,3,3]], axis=0)
newArray=np.append((twoDarray), [[1,2,3,4]],axis=0)
print(newArray) 

# access an element of two d array1
def accessElement(array,row,colom):
    if row>=len(array) and colom>len(array[0]):
        return "Error"
    else:
        print( array[row,colom])

accessElement(twoDarray, 1, 2)

# array traversal in two d array11

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(f"value if [{i}, {j}] is {array[i][j]}")
        print("\n ____________________________________________ ")
            
traverseTDArray(twoDarray)





def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return f"[{i}][{j}]"
    else: return 'nothing found'
searchTDArray(twoDarray, 24)



newTDArray=np.delete(twoDarray,0,axis=0)

print(twoDarray,"\n")
print(newTDArray)















