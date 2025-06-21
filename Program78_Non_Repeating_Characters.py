# Find the first non-repeating character in a string

#s = input("Input the string to calculate the non repeating characters: ").split()
# l_s = len(s)
# single_repeating = []
# non_repeating = []
# for c in range(l_s):
#     character = s[c]
#     l_c = len(character)
#     for cr in range(l_c):
#         if character[cr] not in non_repeating:
#             non_repeating.append(character[cr])
#         else:
#             single_repeating.append(character[cr])
#
# print(non_repeating)
# print(single_repeating)


s = input("Input the string to calculate the non repeating characters: ")
dict = {}
result = -1
for char in s:
    if char in dict.keys():
        dict[char] += 1
    else :
        dict[char] = 1

for key in dict:
    if dict[key] == 1:
        result = key
        break
print(result)


