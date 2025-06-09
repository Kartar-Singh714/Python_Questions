# Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N
# whose elements are sums of the corresponding elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9],
# then N should equal [4,6,13].

l1 = input("Enter the Elements in list 1: ").split(" ")
l2 = input("Enter the Elements in list 2: ").split(" ")
l3 = []
sm = 0
if len(l1) == len(l2):
    for i in range(len(l1)):
        if l1[i].replace(".", "").isdigit() and l2[i].replace(".", "").isdigit():
            l1[i] = float(l1[i])
            l2[i] = float(l2[i])
            sm = l1[i]+l2[i]
            l3.append(sm)
        else:
            print("Invalid numbers in the list")
            exit()
    print(l3)
else:
    print("List Lengths are not same")




