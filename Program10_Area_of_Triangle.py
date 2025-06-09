base = input("Enter the base of the triangle: ")
height = input("Enter the height of the triangle: ")

if base.replace('.', '', 1).isdigit() and height.replace('.', '', 1).isdigit():
    base = float(base)
    height = float(height)
    area = 0.5 * base * height
    print(f"The area of the triangle is {round(area, 2)} square units.")
else:
    print("Invalid input. Please enter numeric values.")