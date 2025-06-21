# 20: Print Reverse Number Pattern
# 	1 1 1 1 1
# 	2 2 2 2
# 	3 3 3
# 	4 4
# 	5
num = int(input("Input the range till you want to print the pattern: "))
for i in range(1, num+1):
    for j in range(num-i+1):
        print(i, end= ' ')
    print(" ")