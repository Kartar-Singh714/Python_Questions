# Q2. Given a sequence of string as a sentence, reverse the sentence
# Ex - str1= "My name is Khan"

str1= "My name is Khan"
#rev = ""
for ch in range(len(str1)-1, -1, -1):
    #rev = rev + str1[ch]
    print(str1[ch], end='')
#print(rev)