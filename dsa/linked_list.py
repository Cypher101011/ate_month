#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 11:06:42 2025

@author: a
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(5)
b=Node(3)
c=Node(7)

a.next=b
b.next=c

head=a
print(head.next.data)


# traverselinked list1
def traverselinked(head):
    current=head
    print("\n")
    while current!=None:
        print(current.data,end="->")
        current=current.next
    print("None")
traverselinked(head)


# insertion in linked list1

def insertAtBegining(head,value):
    newNode=Node(value)
    newNode.next=head
    head =newNode
    
def insertAtEnd(head,value):
    newNode=Node(value)
    if head is None:
        return newNode
    current=head
    while current.next is not None:
        current=current.next
    current.next=newNode
    return head

def insertAtIndex(head,value,index):
    newNode=Node(value)
    current=head
    for i in range(index-1):
        current=current.next
        
    newNode.next=current.next
    current.next=newNode
    traverselinked(head)
insertAtIndex(head,2,3)


# delete element in linked list1
def deleteFirst(head):
    head=head.next
    traverselinked(head)
    return head
deleteFirst(head)

def deleteLast(head):
    current=head
    while current.next.next is not None:
        current=current.next
    current.next=None
    traverselinked(head)
deleteLast(head)
        
def deleteAtIndex(head,index):
    current=head
    for i in range(index-1):
        current.next=current
    current.next=current.next.next
    traverselinked(head,5)
