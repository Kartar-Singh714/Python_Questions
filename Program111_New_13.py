# 13: Print multiplication table from 1 to 10

for number in range(1, 11):
    for num in range(1, 11):
        print(f"{num * number}", end=' ')
    print(" ")