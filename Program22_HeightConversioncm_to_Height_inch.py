# Write a program that asks for your height in centimetres and then converts your height to feet and inches.
# (1 foot = 12 inches, 1 inch = 2.54 cm).

height_cm = input("Please enter the height in cm: ")

if height_cm.replace(".", "").isdigit():
    height_inch = round(float(height_cm)/2.54, 2)
    height_foot = round(height_inch/12, 2)
    print(f"Your Height in inch is = {height_inch} \nYour height in ft is = {height_foot} ")
else:
    print("PLease enter valid input.")
