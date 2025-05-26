a=19
b=20
c=a+b
print("addition of two numbers:",c)

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
def add_numbers(num1,num2):
    return num1+num2
print("the sum of the two numbers is:",add_numbers(num1,num2))

#another way to add two nubers
def add_numbers_alternative():
    num1=int(input("enter any number: "))
    num2=int(input("enter any number: "))
    return num1+num2
print("the sum of two numbera is:",add_numbers_alternative())


#using lamda function to add two numbers
add_numbers_lambda = lambda x, y: x + y
num1=int(input("enter any number: "))
num2=int(input("enter any number: "))
print("the sum of two numbers is : ",add_numbers_lambda)
