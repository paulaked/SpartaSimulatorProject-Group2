# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:45:41 2021

@author: lille
"""

import time

def time_counter(t):

    while t != 0:
        years, months = divmod(t, 12)
        timer = '{:02d}:{:02d}'.format(years, months)
        print(timer, end="\r")
        print(t)
        time.sleep(1)
        t -= 1

    print("The time simulation is over")


t = input("Enter the time in months for the programme to run: ")


#To make sure that it runs until a valid number is given
while True:
    try:
        #ensures that value can be inted
        time_counter(int(t))
        break
    except ValueError:
        #gives a more clear message on what is a valid input
        print("Please enter a number in numeric digits e.g. 2 not two.")
        t = input("Enter the time in months for the programme to run: ")
