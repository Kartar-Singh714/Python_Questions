s = input("Enter the string: ")
dict = {}
m_val = []
mx_key=""
for char in s:
    if char == " ":
        continue
    elif char in dict.keys():
        dict[char] += 1
    else:
        dict[char] = 1

print(dict)
m_val = max(dict.values())
for key, val in dict.items():
    if val == m_val:
        mx_key = mx_key + key

print(mx_key)

