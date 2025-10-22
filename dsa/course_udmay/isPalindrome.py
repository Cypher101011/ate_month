#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 20:47:51 2025

@author: a
"""

def isPalindrome(num):
    reverse=0
    org=num
    if num<0:
        return 
    else:
        return isPalindrome(num%10)+isPalindrome(num/10)