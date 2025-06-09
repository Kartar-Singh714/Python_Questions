#WAP to generate the random OTP of the length entered by the user.

import random
num = input("Please enter the length of the OTP: ")
ran_OTP=0
final = ''
if num.isdigit():
    for i in range(int(num)):
        ran_OTP = random.randint(0, 9)
        final = final + str(ran_OTP)
    print(final)
else:
    print("Invalid Number for OTP generation")