num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
fact_1 = []
fact_2 = []
com = []
for i in range(1, num_1+1):
    if num_1 % i == 0:
        fact_1.append(i)
print(fact_1)
for i in range(1, num_2+1):
    if num_2 % i == 0:
        fact_2.append(i)
print(fact_2)
for i in fact_1:
    for j in fact_2:
        if i == j:
            com.append(i)
print(com)
print(max(com))
