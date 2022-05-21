# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:33:43 2022

@author: Anton
"""

"""

Part A: Househunting 

"""


portion_down_payment=0.25

def MonthsA():
    annual_salary=int(input("Enter your salary:"))
    portion_saved=float(input("Enter the percent of salary you want to save, as a decimal:"))
    total_cost=int(input("Enter the cost of your dream home:"))
    
    
    down_payment=total_cost*portion_down_payment
    monthly_salary=annual_salary/12
    monthly_savings=monthly_salary*portion_saved
    NumberOfMonths=0
    current_savings=0
    r=0.04
    
    while current_savings<=down_payment:
        savings_yield=current_savings*r/12
        current_savings=current_savings+monthly_savings+savings_yield
        NumberOfMonths+=1
    print("Number of months: ", NumberOfMonths)
    
    
    
"""

Part B: Saving, with a raise 

"""
portion_down_payment=0.25

def MonthsB():
    annual_salary=int(input("Enter your salary:"))
    portion_saved=float(input("Enter the percent of salary you want to save, as a decimal:"))
    total_cost=int(input("Enter the cost of your dream home:"))
    semi_annual_raise=float(input("Enter the semiannual raise, as a decimal:"))
    
    down_payment=total_cost*portion_down_payment
    NumberOfMonths=0
    current_savings=0
    r=0.04
    listk=[*range(0,1000,6)]
    listk.remove(0)
    
    
    while current_savings<=down_payment:
            savings_yield=current_savings*r/12
            current_savings=current_savings+(annual_salary/12*portion_saved)+savings_yield
            NumberOfMonths+=1
            if NumberOfMonths in listk:
                print(NumberOfMonths)
                annual_salary=annual_salary+annual_salary*semi_annual_raise
                print(annual_salary)
       
    print("Number of months: ", NumberOfMonths)
    
    

"""

Part C: Finding the right amount to save away

"""

portion_down_payment=0.25

def MonthsC(portion_saved):
    annual_salary=int(input("Enter your salary:"))
    
    total_cost=1000000
    semi_annual_raise=0.07
    
    down_payment=total_cost*portion_down_payment
    NumberOfMonths=0
    current_savings=0
    r=0.04
    listk=[*range(0,1000,6)]
    listk.remove(0)
    
    
    while current_savings<=down_payment:
            savings_yield=current_savings*r/12
            current_savings=current_savings+(annual_salary/12*portion_saved/10000)+savings_yield
            NumberOfMonths+=1
            if NumberOfMonths in listk:
                print(NumberOfMonths)
                annual_salary=annual_salary+annual_salary*semi_annual_raise
                print(annual_salary)
       
    print("Number of months: ", NumberOfMonths)
    
    














