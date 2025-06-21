num = input("Please enter number: ")
arm= 0
cube = 0
sum = 0
for i in range(len(num)):
    cube = int(num[i])**3
    sum = sum +cube
if sum == int(num):
    print("Arm")
else:
    print("Not")
