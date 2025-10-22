#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 17:12:24 2025

@author: a
"""

class Solution(object):
    def gcdOfStrings(self,str1,str2):
        if str1+str2!=str2+str1:
            return ''
        
        def find_gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        gcd_len=find_gcd(len(str1), len(str2))
        
        return str1[:gcd_len]
    
x=input().strip()
y=input()
sol=Solution()
print(sol.gcdOfStrings(x, y))