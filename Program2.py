## Program to find the Prime between the given range
from math import ceil

start = input("Please enter the starting range: ")
ending = input("Please enter the ending range: ")

if start.isdigit() and ending.isdigit():
    for num in range(int(start), int(ending)+1):
        if num > 1 :
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                print(num)
else:
    print("Invalid Input")