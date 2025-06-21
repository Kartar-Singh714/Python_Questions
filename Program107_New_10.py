# 10: Merge two lists using the following condition
#     - list1 = [10, 20, 25, 30, 35]
#     - list2 = [40, 45, 60, 75, 90]
#     - result list: [25, 35, 40, 60, 90]

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []
for i in list1:
    if i%2!=0:
        new_list.append(i)
for i in list2:
    if i%2 == 0:
        new_list.append(i)
print(new_list)