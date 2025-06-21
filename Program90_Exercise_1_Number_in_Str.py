# Q1. In a given string find the word which has a digit in it.
# Ex- str1 = My email is karan50 and its unique

str1 = ("My email is karan50 and its unique kartar40 prabh34deep 40 ").split(" ")
#l = str1
num = ['0', '1', '2', '4', '5', '6', '7', '8', '9']
for word in str1:
    for char in word:
        if char in num:
            print(word)
            break
        else:
            continue


