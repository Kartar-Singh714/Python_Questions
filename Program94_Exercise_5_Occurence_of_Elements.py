# Q5. Count the occurrences of each element in a list
l = list(input("Please enter the number: ").split(" "))
dict = {}

for num in l:
    if num in dict.keys():
        dict[num] +=1
    else:
        dict[num] = 1
print(f"Count is: {dict}")