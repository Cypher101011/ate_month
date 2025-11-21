#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:51:04 2025

@author: a
"""

# doubly linked list

class DoublyNode:
    def __init__(self,data):
        
        self.data=data
        self.prev=None
        self.next=None

a =DoublyNode(5)
b=DoublyNode(3)
c=DoublyNode(7)
a.next=b
b.prev=a
b.next=c
c.prev=a