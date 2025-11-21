#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 17:15:07 2025

@author: a
"""

from typing import Optional

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

a = ListNode(5)
b = ListNode(6)
c = ListNode(7)
d=ListNode(8)
e=ListNode(9)
a.next = b
b.next = c

head = a

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l = 0
        
        # ✅ Corrected condition syntax: "while curr is not None"
        while curr is not None:
            curr = curr.next
            l += 1
        
        curr = head
        
        # ✅ Move curr to middle
        for i in range(l // 2):
            curr = curr.next
        
        return curr


# Example usage
sol = Solution()
mid = sol.middleNode(head)
print("Middle node value:", mid.data)
head=a
def printLL(head):
    curr=head
    while curr:
       
        print(curr.data,end="->" if curr.next else "\n")
        curr=curr.next
        
def fastandSlow(head):
    fast=slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def deleteNode(pointer,head):
    if pointer or pointer.next:
        return
    node=pointer
    node.data=node.next.data
    node.next=node.next.next
    printLL(head)

def deleteNthNode(head,index):
    dummy=ListNode(0)
    dummy.next=head
    p1=p2=dummy
    p1=head
    p2=head
    
    for i in range(index):
        p2=p2.next
        
    if p2==None:
        head=head.next
        return head
    while p2.next:
        p2=p2.next
        p1=p1.next     
        
    
    
deleteNthNode(head,3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    