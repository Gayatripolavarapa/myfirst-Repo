# Print * instead of vowels rom given string
'''
str1="Hi My name is Gayatri"
i=0
Vowels="aeiouAEIOU"
while i<len(str1):
    if str1[i] in Vowels:
        print ('*', end="")
    else:
        print(str1[i], end="")
    i=i+1
'''

#Print each nd every digit from a number in a new line
'''
num=1234
while num>0:
    res=num%10
    print(res)
    num=num//10'''

#Print How to check a number is palindrome or not
'''
pal=121
temp=pal
out=0
while pal>0:
    res=pal%10
    out=out*10+res
    pal=pal//10
if temp==out:
     print("its a palindrome number")
else:
     print("its not a palindrome number")'''

# How to print palindrome number
'''
pal= 121
Out=0
while pal>0:
    res=pal%10
    Output=Out*10+res
    pal//=10
    print(Output)
'''

# How to print palindrome numbers
'''
for num in range(1,100):
 if str(num)==str(num)[::-1]:
  print(num)

'''

'''
num=15
i=1
count=0
while i<=num:
       if num%i==0:
           count+=1
       i+=1
if count==2:
        print("prime number")
else:
        print("not a prime number") '''

#Print a string is palindrome or not

s=input("Enter the string")
if s==s[::-1]:
    print("it's a palindrome")
else:
    print("not a palindrome")

