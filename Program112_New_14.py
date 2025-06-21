# 14: Print a downward half-pyramid pattern of stars
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *

for i in range(5, -1, -1):
    for j in range(i):
        print("*", end = '')
    print(" ")