#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 11:10:26 2025

@author: a

"""
'''
7.8 make a slist call sandwich_orders and fill it with names fo tvarious sandwitches
loop through tlist of sandwich order and print message for each order and as i amd
i mae move it to the list of sandwiches afet all the sandwiches have been print a message
listing each sandwich that made

'''
sandwich_orders=['burger','pizza','nothing','garlig']
finish_order=[]
while sandwich_orders:
            order=sandwich_orders.pop()
            print(f'your order {order} has been placed')
            finish_order.append(order)

print(finish_order)
'''
7.9 no pastrami using the list sandwich order from exercies 7.8 make sure the 
the sandwich pastrami appers in the list at least three Times add code near the
begining of you program to print a message saying the deli has run our pastrami 
and then use a while loop to remove all occurrence of pastrami from sandwich_orders
make usr no pastrai sandwiche end up in finish orders
'''
sandwich_orders=['burger','pizza','nothing','garlig',
                 '\pastrami','pastrami','pastrami']
finish_order=[]
while sandwich_orders:
            order=sandwich_orders.pop()
            print(f'your order {order} has been placed')
            finish_order.append(order)

print(finish_order)