#WAP to print the Number Pyramid
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = 5
count = ''
for i in range(1, num+1):
    count = count + str(i) + ' '
    print(count)

