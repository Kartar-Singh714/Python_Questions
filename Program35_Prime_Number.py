from math import ceil

#num = int(input("Please enter the number: "))

####### Approach 1 #######
# def check_prime(num):
#     int(num)
#     is_prime = True
#     if num == 1:
#         is_prime = False
#     for i in range (2, num):
#         if num%i==0:
#             is_prime = False
#     if is_prime:
#         print(f"{num} is prime number")
#     else:
#         print(f"{num} is not prime number")

# check_prime(int(num))

####### Approach 2 #######
# def ch_prime(num):
#     if num< 2:
#         return False
#     else:
#         for i in range(2, ceil(num/2)-1):
#             if num%i == 0:
#                 return False
#             else:
#                 return True
# print(f"{num} is Prime Number." if ch_prime(num) else f"{num} is not prime"  )
#
# ####### Approach 3 #######
#
num = int(input("Please enter the number: "))
is_prime = True
def check_pr(num):
    if num>2:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
    else:
        is_prime = True

check_pr(num)

print(f"{num} is Prime" if is_prime else print(f"{num} is not prime number."))






