# Python program to find average of five numbers

# take inputs
num1 = 6
num2 = 1
num3 = 2
num4 = 5
num5 = 3

# calculate average
avg = (num1 + num2 + num3 + num4 + num5) / 5

# print average value
print('The average of numbers = %0.2f' %avg)


#Python program to find num is odd or even

num=int(input('enter num'))

if (num%2)==0:
    print('Number is even',num)
else:
    print('Number is odd',num)

#print year is loop year or not

year=int(input("Enter a year:"))
if(year%4) == 0:
    if(year%100) == 0:
        if(year%400) == 0:
            print("{0}is a leap year".format(year))
        else:
             print("{0}is a not leap year".format(year))
    else:
            print("{0}is a leap year".format(year))
else:
    print("{0}is a not leap year".format(year))


#check num is neg or posi
num = float(input("Enter a number: ")) 
if num > 0:  
 print("Number is a positive number")  
elif num == 0:  
   print("Number is zero")   
else:  
   print("Number is negative number")   

#check the largest num or equal
num1 =int(input('enter num1'))
num2=int(input('enter num2'))
if num1>num2:
    print('n1 is gretest')
elif num1==num2:
    print('number is equal')
else:
    print('n2 is gretest')


# Python program to find the factorial of a number provided by the user
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

# program to swap 2 numbers using third variable.
num1=int(input('Enter a Number'))
num2=int(input('Enter a Number'))
temp=num1
num1=num2
num2=temp
print('The value of x after swapping: {}'.format(num1))
print('The value of y after swapping: {}'.format(num2))


#check the Smallest num
from typing import Sequence
num1 =int(input('enter num1'))
num2=int(input('enter num2'))
if num1<num2:
    print('n1 is Smallest')
else:
    print('n2 is Smallest')

#Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.
num=int(input('enter a number'))
if num<100:
    if (num%2)==0:
        print('Number is even')
    else:
      print('Number is odd')
else:
    print('Number is greter then 100'.format(num))

#take number and print the square
num=float(input('enter a number'))
if num<10:
    square = num * num
print("The Square of a Given Number {0}  = {1}".format(num, square))

#check number is neg or positive using nested if else
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


#print the large number
num1= int (input('enter a num1'))
num2= int (input('enter a num2'))
num3= int (input('enter a num3'))
if num1>num2:
    if num1>num3:
        print('num1 is greter')
    else:
        print('num3 is greter')
else:
    if num2>num3:
        print('num2 is greter')
    
    else:
        print('num3 is greter')


# numbers and find smallest number using logical operator
num1=int(input("Enter the first number: ")) 
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: ")) 
if(num1<=num2 and num1<=num3): 
  print(num1," is the smallest")

elif(num2<=num1 and num2<=num3):
  print(num2," is the smallest")

else:
    print(num3," is the smallest")

#swapping without using third veriable
x = int(input("Enter the value of x"))  
y = int(input("Enter the value of y"))  
print("before swapping numbers: %d   %d\n" %(x,y))  
#swapping#  
x = x + y     
y = x - y    
x = x - y     
print("After swapping: %d   %d\n"%(x,y))  