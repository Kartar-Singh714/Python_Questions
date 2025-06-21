# 2: Print the Sum of a Current Number and a Previous number

c_no, p_no, s = 0, 0, 0
r = int(input("Please enter the range: "))
print(f"Printing current and previous number sum in a range({r}) ")
for i in range(r):
    s = p_no+c_no
    print(f"Current Number {c_no} Previous Number  {p_no}  Sum:  {s}")
    p_no = c_no
    c_no+=1
