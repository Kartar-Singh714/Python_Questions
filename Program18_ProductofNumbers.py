num = input("Enter a number: ")

if num.isdigit():
    product = 1
    for digit in num:
        product *= int(digit)
    print(f"Product of digits = {product}")
else:
    print("Invalid input. Please enter a positive number.")