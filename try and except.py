# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:12:50 2021

@author: lille
"""

t = input("Enter number: ")
while True:
    try:
        a =int(t)
        break
    except ValueError:
        print("Please enter a number in numeric digits")
        t = input("Enter number: ")

    
print(a)
    
