# 1: Calculate the multiplication and sum of two numbers
# 	Given two integer numbers, write a Python program to return their product
# 	only if the product is equal to or lower than 1000. Otherwise, return their sum.

num1 = int(input("Please enter First number: "))
num2 = int(input("Please enter Second number: "))
p = num1*num2
if p<=1000:
    sum = num1 + num2
    print(f"Sum of the Digits is: {sum}")
else:
    print(f"Product of the Digits is: {p}")