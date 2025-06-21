#Count how many times the digit 7 appears from 1 to N
count = 0
num = input("Enter the number: ")

for i in range(1, int(num)+1):
    t = str(i)
    for ch in t:
        if ch == '7':
            count+=1
    else:
        continue

print(count)

