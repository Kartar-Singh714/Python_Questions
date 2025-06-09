#Write a program that inputs two lists and creates a third,
# that contains all elements of the first followed by all elements of the second.

l1 = input("Please enter the List 1 using seprated by Comma',': ").split(",")
l2 = input("Please enter the List 2 using seprated by Comma',': ").split(",")
l3 = []

l3 = l1+ l2
print(l3)

#Second approach
# for i in l1:
#     l3.append(i)
# for i in l2:
#     l3.append(i)
# print(l3)