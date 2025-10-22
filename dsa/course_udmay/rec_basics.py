#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 12:42:38 2025

@author: a
"""

def A():
    s=1
    return 'hello '+B()
    
def B():
    return 'my ' +C()

def C():
    return 'friends'

print(A())