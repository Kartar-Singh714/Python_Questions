num = input("Enter a number: ")

if num.replace('.', '', 1).isdigit():
    num = float(num)
    if num >= 0:
        sqrt = num ** 0.5
        print(f"Square root of {num} is {round(sqrt, 2)}")
    else:
        print("Square root of negative number is not real.")
else:
    print("Invalid input. Please enter a numeric value.")