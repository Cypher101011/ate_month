#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 11:52:09 2025

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
class Solution:
    def deleteDuplicates(self,head):
        if head ==None or head.next==None:
            return None
        curr=head
    
        while curr.next:
            if curr.data==curr.next.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        
        return head
    
sol=Solution()
sol.deleteDuplicates(head)

class DUPLICATE:
    def deleteDuplicates(self,head):
        if head or head.next:
            return 