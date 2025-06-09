a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"Largest is: {a}")
elif b >= c:
    print(f"Largest is: {b}")
else:
    print(f"Largest is: {c}")