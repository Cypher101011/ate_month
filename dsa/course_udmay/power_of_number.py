#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 20:00:12 2025

@author: a
"""
def power(base,exp):
    # assert exp>=0 and int(exp)==exp,'the exponent must be interger only'
    if exp==0:
        return 1
    if exp==1:
        return base
    if exp<0:
        return (1/base) * power(base,exp+1)
    if exp>0:
        return base * power(base,exp-1)
    
power(-2,3)