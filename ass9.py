#. Program to check if a number is a 3-digit number or not?
digit=input("Enter any three digit number:")
if digit.isdigit() and 100 <= int(digit) <= 999:
    print("This is 3 digit number ")
else:
    print("This is not a three digit number ")    

    