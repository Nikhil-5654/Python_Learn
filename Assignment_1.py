# Task 1

a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))

print('Addition:', a + b)
print('Subtraction:', a - b)
print('Multiplication:', a * b)
print('Division:', a / b)

""" OUTPUT
Enter your first number: 5
Enter your second number:10
Addition: 15
Subtraction: -5
Multiplication: 50
Division: 0.5"""

#Task 2

def string(first_name):
    return first_name


First_Name = string(input('Enter Your First Name: '))
Last_Name = string(input('Enter Your Last Name: '))
print('Hello,' , First_Name,'!' , Last_Name,'! Welcome to the Python Program')