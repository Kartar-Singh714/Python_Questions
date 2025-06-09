count=5
#while count>0:  print(count);     count-=1
# while count>0:
#     print(count)
#     count-=1
#     if count==2:
#         break
# else:
#     print("In else block")
# print("Out from loop")

num = int(input("Enter the number: "))
s = 0
# while num != -1:
#     print(num)
#     num = int(input("Enter the number and press -1 to quit"))
# else:
#     print("In else block")
# print("Out of while loop ")

while num !=0:
    s = num+ s
    num = int(input("Enter the number: "))
print(s)
