#Remove Spaces without using replace function.

#s = "Hello World"
s = input("Please enter the string: ")

without_spaces=''
for c in s:
    if c != " ":
        without_spaces+=c
    else:
        continue

print(without_spaces)
