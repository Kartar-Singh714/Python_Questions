st = input("Enter the String: ")
l=0
l1=0
for i in st:
    l+=1
    if i == " ":
        st.replace(" ", "")
        l-=1
    l1+=1
print(f"The count of the string is {l}")
print(f"The count of the string without whitespaces is {l1}")