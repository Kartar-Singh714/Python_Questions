# WAP to find out Armstrong number
# An Armstrong number is a number that equals the sum of its digits,
# each raised to the power of the number of digits in the original number.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

num = input("Enter the Number: ")
l = len(num)
s ,c = 0, 0
if num.replace(".", "").isdigit() or num == 0:
    for i in num:
        c = int(i)**l
        s = s+c
    if s == int(num):
        print(f"{num} is the Armstrong number")
    else:
        print(f"{num} is not the Armstrong Number")
else:
    print("Invalid Number")

