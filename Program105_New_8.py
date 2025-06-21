# 8: Print the following pattern
#     - 1
#       2 2
#       3 3 3
#       4 4 4 4
#       5 5 5 5 5

num = int(input("Please enter the number: "))
# for n in range(0, num+1):
#     for i in range(0, n):
#         print(n, end = " ")
#     print("")
############## Solution 2 #################
for n in range(num+1):
    for i in range(n):
        print(n, end = " ")
    print("")