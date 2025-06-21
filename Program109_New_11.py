# 11: Get each digit from a number in the reverse order.
# 	- number = 7536
# 	  # Output 6 3 5 7

num = input("Enter the number: ")

for i in range(len(num)-1, -1, -1):
    print(num[i], end="  ")