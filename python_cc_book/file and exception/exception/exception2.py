#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 10:14:52 2025

@author: a
"""

# word_count.py

from pathlib import Path

def count_words(path):
    '''count the approximate number of the words in a file'''
    try:
        contents= path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"sorry,the file {path} not found ")
    else:
        #count the approximate number of words in the file
        words=contents.split()
        num_words=len(words)
        print(f"the file{path} has about {num_words} words.")
        path=Path('shekspier.txt')
        count_words(path)


