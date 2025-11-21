#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 12:31:14 2025

@author: a
"""

# REMOVE DUPLICATE FROM LIKED list
class Node:
    def __init__(self,data,next=None):
            self.data=data
            self.next=next
            
a=Node('a')

b=Node('b')
c=Node('c')
d=Node('a')
head=a
a.next=b
b.next=c
c.next=d

def printLL(head):
    curr=head
    while curr:
        print(curr.data,end='->')
        curr=curr.next
    print('None')
    
printLL(head)

def reverseLL(head):
    curr=head
    prev=None
    nxt=None
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    printLL(prev)
    return prev

reverseLL(head)