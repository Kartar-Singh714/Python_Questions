height = input("Please enter the heights: ")
h_list1 = []
len_list, sum = 0, 0

if height.replace(",", "").replace(".", "").isdigit():
    h_list1 = height.split(",")
    # for h in height.split(","):
    #    h_list1.append(float(h))
    for i in h_list1:
        len_list+=1
        sum+=float(i)
    avg = sum / len_list
    print(f"The average height is the: {round(avg)}")
else:
    print("Invalid Input")



