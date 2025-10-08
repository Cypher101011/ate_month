#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 11:23:08 2025

@author: a
"""

StringEqual(str1,str2):
        if len(str1)!=len(str2):
            return False
        while i<len(str1) and str[i]==str2[i]:
            i+=1 
        return i==len(str1)

StringEqual('lucifer','morningstar')