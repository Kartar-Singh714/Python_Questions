s = input("Enter the String: ").lower()
dict ={}
result = ""
for char in s:
    if char in dict.keys():
        dict[char] +=1
    else:
        dict[char] = 1
for key in dict:
    if dict[key] == 1:
        result = result + key
print(result)
