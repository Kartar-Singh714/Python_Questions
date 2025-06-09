import random
rock, paper, sc = 0, 1, 2
u_input = input("Please select the option:\nRock = 0\nPaper = 1\nScissor = 2\nPlease enter your choice: ").strip()

com_response = random.randint(0, 2)
print(f"Computer's response: {com_response}")

if u_input.isdigit():
    u_input = int(u_input)
    if 0 <= u_input <= 2:
        #print(f"")
        if (u_input == rock and com_response == rock) or (u_input == paper and com_response == paper) or (u_input == sc and com_response == sc):
            print("Tie")
        elif (u_input == rock and com_response == sc) or (u_input == paper and com_response == rock) or (u_input == sc and com_response == paper):
            print("You Won")
        else:
            print("You loose")
    else:
        print("You Loose Wrong Input. It should be 0, 1 or 2")
else:
    print("Invalid Input")






