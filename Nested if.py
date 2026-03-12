#Nestedif - if within another if statement, usefull when need to check for second condition, only if the first one is True
###Syntax###
'''if condition1:
    #Executes if condition is True
if condition2:
    #Executes if condition1 and Condition2 is True
else:
    #Executes if condition1 is True but Condition2 is False
else:
    #Executes if condition1 is False'''

#Example 1
'''
cricket=input("Enter the mode of cricket")
if cricket:
    if cricket=='One-day match':
        print("You are watching One-day match")
    elif cricket=='20-20 match':
        print("You are watching 20-20 match")
    elif cricket=='Test match':
        print("You are watching Test match")
else:
    print("You are not watching any match") '''

#Example 2
'''
Fruits=("Grapes","Apples","Peaches","Oranges")
Fruit=input("Enter the Fruit")
if Fruit in Fruits:
    if Fruit=='Grapes' or Fruit=='Apples':
        print("Its my favorite fruits")
    elif Fruit=='Peaches' or Fruit=='Oranges':
        print("Its my favorite fruits")
    elif Fruit=='Oranges':
        print("Its my favorite fruits")
else:
    print("Others fruits are not my favorite fruits")'''

#Example 3

Cars=("Benz","Alto","Hyundai")
Car=input("Enter the Car")
if Car in Cars:
    if Car=='Benz':
        print("Its my favorite car")
    elif Car=='Alto':
        print("Its my favorite car")
    elif Car=='Hyundai':
        print("Its my favorite car")
else:
        print("Others cars are not my favorite car")




