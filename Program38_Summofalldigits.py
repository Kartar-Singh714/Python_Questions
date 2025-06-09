num = input("Enter a number: ")
total = 0
final = 0
for digit in num:
    total += int(digit)
print(total)
for t in str(total):
    final+=int(t)
print("Sum of digits:", final)