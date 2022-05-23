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
semi_annual_raise=0.07
r=0.04                        
down_payment=250000

annual_salary1=int(input("Enter the starting salary:"))

def PortSave(portion_saved):
    
    annual_salary=annual_salary1
    savings=0
    month_untill_finish=0
    
    
    listk=[*range(0,1000,6)]
    listk.remove(0)
    
    while savings-100<down_payment or savings+100<down_payment:
        savings_yield=savings*r/12
        savings=savings+savings_yield+(annual_salary/12*portion_saved/10000)
        month_untill_finish+=1
        if month_untill_finish in listk:
            annual_salary=annual_salary+annual_salary*semi_annual_raise
    return month_untill_finish



num=0
xmin=0
xmax=10000
num=0

x=(xmax+xmin)/2 

while PortSave(x)!=36:
    num+=1
    if int(x)==xmax:
        print("It is not possible to pay the down payment in three years.")
        break
    elif PortSave(x)>36:
        xmin=x
    elif PortSave(x)<36:
        xmax=x
    x=(xmax+xmin)/2
    
        
print("Best savings rate:", x/10000, "NumGuesses:",num)
        
    













