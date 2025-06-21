# 5: Check if the first and last numbers of a list are the same

list1 = list(input("Please enter the list by giving spaces: "))
len = len(list1)

def check(list1):
    if list1[0] == list1[len-1]:
        return True
    else:
        return False

print(check(list1))