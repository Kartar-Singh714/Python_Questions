nums = [12, -5, 0, -2, 6, 7, -9]
positive = 0
negative = 0

for n in nums:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)