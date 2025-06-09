numbers = input("Enter the number separated with the comma',' to calculate the square: ").split(",")
squares = []
for num in numbers:
    if num.replace(".", "").isdigit():
        f = float(num)
        squares.append(f ** 2)
    else:
        print(f"{num} is not a valid number.")

print(squares)
