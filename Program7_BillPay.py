import random

people = input("Enter the name of the 5 persons separated by comma: ")
people_list = people.split(", ")
print(people_list)
#print(f"{random.choice(people_list)} will pay the bill.)  ## 1st Way
##2nd way
len = len(people_list)
r = random.randint(0, len-1)
print(f"{people_list[r]} will pay the bill.")
#3rd Way
# if r == 0:
#     print(people_list[0])
# elif r==1:
#     print(people_list[1])
# elif r==2:
#     print(people_list[2])
# elif r==3:
#     print(people_list[3])
# elif r==4:
#     print(people_list[4])