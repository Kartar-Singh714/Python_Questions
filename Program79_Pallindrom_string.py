#Write a function that returns True if a string is a palindrome, ignoring case and spaces

s = input("Enter the string: ")
normal_s = ""
pal = ""
for c in range(len(s)):
    if c == " ":
        continue
    normal_s = normal_s + s[c].lower()
for r in range(len(normal_s)-1, -1, -1):
    pal = pal + s[r].lower()


if normal_s == pal:
    print("True")
else:
    print("False")





