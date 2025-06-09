yr= int(input("Enter the year"))

if yr % 4 == 0 or yr %100 != 0:
        if yr % 400 == 0:
            print(f"{yr} is a Leap Year")
        else:
            print(f"{yr} is not a Leap Year")
else:
    print("Not a Leap Year")