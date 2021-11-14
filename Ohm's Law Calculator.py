# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:35:27 2020

@author: HarukiKazuya
"""

import sys
def prompt_virq():
    keyinput = ''
    options = ['V','I','R','Q']
    while keyinput not in options:
        keyinput = raw_input("Please enter 'v', 'i', 'r' or 'q': ").upper()
    return keyinput
def cal_v():
    I = float(input('Please input I: '))
    R = float(input('Please input R: '))
    V = I*R
    return V,'V'
def cal_i():
    V = float(input('Please input V: '))
    R = float(input('Please input R: '))
    I = V/R
    return I,'I'
def cal_r():
    V = float(input('Please input V: '))
    I = float(input('Please input I: '))
    R = V/I
    return R,'R'
def print_result(name,value):
    print name,'= %.2f'%(value)
    
inputstr = prompt_virq()
while True:
    if inputstr == 'Q':
        print "Bye!"
        sys.exit()
    elif inputstr == 'V':
        value,name = cal_v()
        print_result(name,value)
    elif inputstr == 'I':
        value,name = cal_i()
        print_result(name,value)
    elif inputstr == 'R':
        value,name = cal_r()
        print_result(name,value)
    inputstr = prompt_virq()