#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 20:07:53 2025

@author: a
"""

def power(base,exp):
    if exp==0 or base==1:
        return 1
    if exp<0:
        return (1/base)* power(base,exp+1)
    else:
        return base *power(base,exp-1)
    
power(2,-2)

def powerNO(base,exp):
    result=1
    if exp==0 or base==1:
        return 1
    else:
        for i in range(exp):
            result*=base
    return result

powerNO(10,3)