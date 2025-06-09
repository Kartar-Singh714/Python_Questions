#Write a program to check if a number is present in the list or not. If the number is present, print the position of the number.
# Print an appropriate message if the number is not present in the list.
#st_list = [1,22,3,4,95,6,7,8,9,10,11,12,13,14,15]

st_list = input("Please neter the list of numbers by giving spaces: ").split(" ")
print(st_list)
num = input("Please enter the number to be searched: ")

if num in st_list:
    pos =st_list.index(num)
    print(f"Number {num} found at {pos+1} position")
   ####Approach2######
    # for i in range(len(st_list)):
    #     #print(i+1, ":", st_list[i])
    #     if st_list[i] == num:
    #         pos = i + 1
    #        print(f"Number {num} found at {pos} position")
else:
    print("Number not found in list")
