def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
operation_menu = ''
res = 0
def get_data():
    a = input("Enter first number: ")
    operation_menu = input("+ \n- \n* \n/ \nPick an Operation: ")
    b = input("Enter second number: ")
    global res
    f_num, s_num = int(a), int(b)
    res = calculate(operation_menu, f_num, s_num)
    return operation_menu, f_num, s_num, res

def calculate(menu, f_num, s_num):
    if menu == "+":
        res = add(f_num, s_num)
        print(f"a + b = {res}")
    elif menu == "-":
        res = sub(f_num, s_num)
        print(f"a - b = {res}")
    elif menu == "*":
        res = mul(f_num, s_num)
        print(f"a * b = {res}")
    else:
        res = div(f_num, s_num)
        print(f"a / b = {res}")
    return res

def calculate_again(res):
    operation_menu = input("+ \n- \n* \n/ \nPick an Operation: ")
    b = input("Enter second number: ")
    s_num = int(b)
    new_res = calculate(operation_menu,res, s_num)
    return operation_menu, new_res, s_num, res

get_data()
choice = input(f"Enter 'y' to continue calculation with {res} or 'n' to start new calculation  or 'x' to exit.").lower()
if choice == 'y':
    calculate_again(res)
elif choice == 'n':
    get_data()
elif choice == 'x':
    exit()
else:
    print("Invalid Choice. Bbye")
    exit()

