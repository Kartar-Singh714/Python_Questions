str1 = ("Emma is caring, Emma is writer").lower()
l = str1.split(" ")
s_tobe_Found = input("Please enter string to be found: ")
count = 0
for word in l:
    if word == s_tobe_Found:
        count += 1
    else:
        continue
print(f"{s_tobe_Found} appeared {count} times")