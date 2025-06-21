# 17: Generate Fibonacci series up to 15 terms
num = int(input("Please enter the number to which you want to generate fibonacci series: "))
prev = 0
cur = 1
sum = 0
print(prev, end= ' ')
print(cur, end= ' ')
for num in range(2, num):
        sum = prev + cur
        print(sum, end= ' ')
        prev = cur
        cur = sum

