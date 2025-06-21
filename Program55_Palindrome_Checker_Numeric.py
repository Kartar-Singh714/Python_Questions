num = input("Please enter the number: ")
p_num = ""
for i in range(len(num)-1, -1, -1):
    p_num += num[i]
if p_num == num:
    print("Palindrome")
else:
    print("No")