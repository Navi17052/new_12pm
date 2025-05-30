# Write a program to find the biggest of given 3 numbers from the command prompt?
num1=input("enter any first number:")
num2=input("enter any second number:")
num3=input("enter any third number:")
if num1>num2 and num1>num3:
    print("first number is bigger")
elif num2>num1 and num2>num3:
    print("second number is bigger")
else :
    print("third number is bigger")        