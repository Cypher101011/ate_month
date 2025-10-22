#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 12:11:10 2025

@author: a
"""

def decimal_to_binary(n):
     assert int(n)==n,'the parameter must be an integers'
     if n==0:
         return 0
     else:
         return n%2 +10 * decimal_to_binary(int(n/2))


decimal_to_binary()