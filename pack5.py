# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:44:39 2022

@author: Anton
"""
'''
Finger exercise: Implement a function that calculates the probability of rolling
exactly two 3’s in k rolls of a fair die. Use this function to plot the probability as k
varies from 2 to 100.
'''
import matplotlib.pyplot as plt

def factorial(k):
    i=1
    f=k
    while i<k:
        f=f*i
        i=i+1
    return f

def prob(k):    
    prob=(factorial(k)/(factorial(2)*factorial(k-2)))*((1/6)**2)*((5/6)**(k-2))
    return prob

listk=[]
k=3

while k<101:
    listk.append(prob(k))
    k=k+1
 
    
 
plt.plot(listk)   
plt.show() 