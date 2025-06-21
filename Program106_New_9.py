# 9: Check Palindrome Number

num = input("Enter number: ")
p_num = ""
for n in range(len(num)-1, -1, -1):
    p_num =  p_num + num[n]

if num == p_num:
    print("Yes Pallindrome")
else:
    print("No Not Pallindrome")
