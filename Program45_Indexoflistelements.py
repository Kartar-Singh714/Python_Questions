list1 = input("Enter the number separated with the comma',' to calculate the square: ").split(",")
element = input("Enter the number for index: ")
if element in list1:
    index = list1.index(element)
    print(f"Index of '{element}' is {index}")
else:
    print(f"'{element}' not found in the list")