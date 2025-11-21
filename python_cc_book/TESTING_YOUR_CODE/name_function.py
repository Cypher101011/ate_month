#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:23:06 2025

@author: a
"""

def get_formatted_name(first,last,middle=''):
    '''generate a neatly formatted full name'''
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name=f'{first} {last}'
    return full_name.title()
