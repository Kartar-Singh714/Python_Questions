# Function for swapping the variables using Third variables.
def first_way_swap(num1, num2):
    tem = 0 # Using third variable
    tem = num1 # temp = 56
    num1 = num2
    num2 = tem
    print(f"After Swapping the numbers through 1st way are {num1} , {num2}")

# Function is for swapping the variables using XOR Operator
def second_way_swap(num1, num2):
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    print(f"After Swapping the numbers through 2nd way are {num1} , {num2}")

# Function is for swapping the variables using arithmetic(+) operators
def third_way_swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print(f"After Swapping the numbers through 3rd way are {num1} , {num2}")

# Function is for swapping the variable using tuples way
def fourth_way_swap(num1, num2):
    (num1, num2) = (num2, num1)
    print(f"After Swapping the numbers through 4th way are {num1} , {num2}")


num1 = int(input("Please enter the First Number: "))
num2 = int(input("Please enter the Second Number: "))
print(f"Before Swap Number are {num1}, {num2} \n")

first_way_swap(num1, num2)
second_way_swap(num1, num2)
third_way_swap(num1, num2)
fourth_way_swap(num1, num2)
