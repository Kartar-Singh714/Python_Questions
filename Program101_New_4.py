# 4: Remove first n characters from a string

def remove_char(word, n):
    new = ""
    for ch in range(n+1, len(word)):
        new = new + word[ch]
    return new

word = input("Enter the String: ")
n = int(input("Enter the number of characters you want to remove: "))
len_str = len(word)
if n <= len_str:
    print(remove_char(word, n))
else:
    print("Number should be less than the string.")