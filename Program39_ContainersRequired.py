from math import ceil

he = input("Please enter the Height of Wall in sq/mt: ")
we = input("Please enter the Width of Wall in sq/mt: ")
cover = 7

def containers_required(height, width, coverage):
    area = height * width
    required = area / coverage
    container = ceil(required)
    print(f"Total containers required = {container}")

if he.isdigit() and we.isdigit():
    # Convert strings to numeric values
    height = int(he)
    width = int(we)
    coverage = float(cover)

    if height > 0 and width > 0 and coverage > 0:
        containers_required(height, width, coverage)
    else:
        print("All values must be greater than 0.")
else:
    print("Invalid input. Please enter valid numbers.")