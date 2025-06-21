vowels = ['a', 'e', 'i', 'o', 'u']
s = input("Enter the string: ").lower()
v_instr = []
without_Vowels = []
for i in s:
    if i == " ":
        continue
    elif i in vowels:
        v_instr.append(i)
    else:
        without_Vowels.append(i)
w_v = str(without_Vowels)
print(w_v)

