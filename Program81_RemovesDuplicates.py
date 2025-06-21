# Remove all duplicates from a list but preserve order
num = input("Please enter the Number: ").split()
l_num = len(num)
dup= []
for n in range(l_num):
    ind = num[n]
    l_ind = len(ind)
    for i in range(l_ind):
        if ind[i] in dup:
            continue
        else:
            dup.append(ind[i])

print(dup)




