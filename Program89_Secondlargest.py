#l=input("Please enter teh numbers: ").split(" ")
l = [2,4,6,8,4]
f = l[0]
s = l[0]

for i in range(len(l)):
    if l[i]>f:
        s = f
        f= l[i]
    elif l[i]>s and s!=l[i]:
        s = l[i]

print(s)