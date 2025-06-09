weight = int(input("Enter your weight "))
height = float(input("Enter you height in ft"))

bmi = weight/(height ** 2)
bmi = round(bmi, 2)
print("Your BMI is ", bmi)
if bmi<18.5:
    print(f"Your BMI is {bmi} and You fall under weight category")
elif bmi>=18.5 and bmi<=24.9:
    print(f"Your BMI is {bmi} and You fall under Normal category")
elif bmi>=25 and bmi<=29.9:
    print(f"Your BMI is {bmi} and You fall under overweight category")
elif bmi>=30.0 and bmi<=39.9:
    print(f"Your BMI is {bmi} and You fall under obese category")
else:
    print(f"Your BMI is {bmi} and You are Obese Class 3")
