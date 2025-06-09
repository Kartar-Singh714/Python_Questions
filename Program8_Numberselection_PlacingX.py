# 1st Way
# lt1 = [1 ,2, 3]
# lt2 = [4, 5, 6]
# lt3 = [7, 8, 9]
# f_list = [lt1, lt2, lt3]
# c = input("Enter the coordinates to which you want to hide money: ")
# a = int(c[0])
# b = int(c[1])
# sub_lt = f_list[a-1]
# sub_lt[b-1] = "X"
# print(sub_lt)
# print(f_list)
# print(f"{lt1}\n{lt2}\n{lt3}")

## Way 2
lt11 = [['😀','😀','😀'], ['😀','😀','😀'], ['😀','😀','😀']]
print(f"{lt11[0]}\n{lt11[0]}\n{lt11[0]}")
i = input("Enter the coordinates to which you want to hide money: ")
x = int(i[0])
y = int(i[1])
lt11[x-1][y-1] = "❌"
print(f"{lt11[0]}\n{lt11[1]}\n{lt11[2]}")

