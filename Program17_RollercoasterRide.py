height = int(input("Enter the Height: "))

if height>3:
    print("You can ride.")
    age = int(input("What is you age: "))
    if age < 12:
        t_price = 150
        print(f"Ticket price is {t_price} rs.")
    elif age > 12 and age <= 18:
        t_price = 250
        print(f"Ticket price is {t_price} rs.")
    elif age > 25:
        t_price = 500
        print(f"Ticket Price is {t_price} rs.")
    photo = input("Do want to click pictures? (y/n)  ")
    if photo == 'y' or photo == 'Y':
        t_price += 50
    print(f"You total bill is {t_price}")
else:
    print("You can't ride")

print("Thank You.. Enjoy the Ride")