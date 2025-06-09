data = [1, 2, 2, 3, 4, 4, 5]
unique = []
for i in data:
    if i not in unique:
        unique.append(i)
print("List without duplicates:", unique)