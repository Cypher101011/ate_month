#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:56:46 2025

@author: a
"""

class CircularNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
a=CircularNode(5)
b=CircularNode(6)
c=CircularNode(7)

a.next=b
b.next=c
c.next=a


head=a

def traverseLinkedList(head):
    curr=head
    while True:
        print(curr.data,end="->")
        curr=curr.next
        if curr==head:
            print("None")
            break
traverseLinkedList(head)