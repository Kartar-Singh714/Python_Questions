a = [1, 2, 3]
b = [1, 4, 3]

for i in range(len(a)):
    if a[i] != b[i]:
        print(f"Element differs at index {i}, as {a[i]} != {b[i]}")