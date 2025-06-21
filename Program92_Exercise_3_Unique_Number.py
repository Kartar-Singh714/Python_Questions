# Q3. Construct an array of numbers by taking input from the user and finally build an array with unique number

l = list(input("Please enter the numbers using spaces: ").split(" "))
uni_list = []

for num in l:
    if num not in uni_list:
        uni_list.append(num)
    else:
        continue
print(uni_list)