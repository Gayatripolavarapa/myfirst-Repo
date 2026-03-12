#Else if ladder

'''Allows to check multiple conditions sequentially and execute code and rest of the ladder or code is entirely skipped'''

# Syntax
'''if condition1:
    # code to execute if condition is True
elif condition2:
    # code to execute if condition is True
elif condition3:
    # code to execute if condition is True
else:
    # code to execute if condition is False/none of the above conditions are True'''

# if colours==("red","blue","orange","pink"):
#     print("Enter the colour")
# elif colours==:
#     print("yes","Its a colour")
# elif "colours"=="blue":
#     print("yes","Its a colour")
# elif "colours"=="orange":
#     print('yes',"Its a colour")
# elif "colours"=="pink":
#     print('yes',"Its a colour")
# else:
#     print("It's not a colour")

#Example 1

'''colors=('red','green','blue')
color=input('enter color')
if color in colors:
    if color=='red':
        print('red')
    elif color=='green':
        print('green')
    elif color=='blue':
        print('blue')
else:
    print('please enter a valid color')'''

#Example 2

'''Marks=int(input('enter Marks'))
if Marks>=90:
    print('student got Grade A')
elif Marks>=80:
    print('student got Grade B')
elif Marks>=70:
    print('student got Grade C')
else:
    print('Student got Grade D')'''

#Example 3

Stations=('Hyd','Chennai',"Pune","Goa")
Station=input("Enter your station")
if Station in Stations:
 if Station=='Hyd':
    print('You have reached your station')
 elif Station=='Chennai':
    print('You have reached your station')
 elif Station=='Pune':
    print('You have reached your station')
 elif Station=='Goa':
    print('You have reached your station')
else:
    print('This is not your station')

