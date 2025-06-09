# A store charges ₹120 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is ₹100 per item.
# If you buy 100 or more items, the cost is ₹70 per item.
# Write a program that asks the user how many items they are buying and prints the total cost.

total = input("Please enter the Total Number of items to buy. ")
cost = 0
if total.isdigit() and int(total)!=0:
    t = int(total)
    if t < 10:
        t *= 120
        print(f"Total Cost = {t}")
    elif 10<=t<=99:
        t *= 100
        print(f"Total Cost = {t}")
    else:
        t *= 70
        print(f"Total Cost = {t}")
else:
    print("Invalid Input")

