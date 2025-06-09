# WAP to find out the count of vowels and consonants in a given word/sentence ignoring spaces.

vowels = ['a','e','i','o','u']
st = input("Please enter the Word/sentence to find out count of vowels: ").lower()
count_vow = 0
count_con = 0
for i in st:
    if i in vowels:
        count_vow+=1
    elif i == " ":
        continue
    else:
        count_con+=1

print(f"Total number of vowels in the string: {count_vow} \nTotal number of consonants in string: {count_con} ")