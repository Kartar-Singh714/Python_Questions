# Ask the user to enter a list containing numbers between 1 and 12.
# Then replace all of the entries in the list that are greater than 10 with 10.

l1 = input("Please enter the number between 1 - 12 separated by Comma ',': ").split(",")

for i in range(len(l1)):
    if l1[i].isdigit():
        l1[i] = int(l1[i])
        if l1[i] >= 1 and l1[i]<=12:
            if l1[i] >10:
                l1[i] = 10
        else:
            print("Numbers should be between 1 to 12")
            exit()
    else:
        print("Invalid Input")
        exit()
print(l1)
