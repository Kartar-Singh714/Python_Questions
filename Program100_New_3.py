# 3: Print characters present at an even index number

str = input("Enter the string: ")

for ch in range(len(str)):
    if ch%2==0:
        print(str[ch])
