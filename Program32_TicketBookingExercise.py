age = input("Please enter your age: ").strip()
day = input("Please enter the day of the week: ").lower()
kids_t_price = 100
adult_t_price = 150
senior_t_price = 80
total = 0
if day == "wednesday":
    total+=20
if age.replace(".", "", 1).isdigit():
    age = float(age)
    print(age)
    if age >=1 and age < 13:
        price = total + kids_t_price
        print(f"Total Price: {price}")
    elif age >=13 and age <= 59:
        price = total + adult_t_price
        print(f"Total Price: {price}")
    elif age >= 59 and age <= 100:
        price = total + senior_t_price
        print(f"Total Price: {price}")
    else:
        print("Invalid age")
else:
    print("Invalid Age")

# s = "hello"
# print(s.replace("l", "p"))
# print(s)