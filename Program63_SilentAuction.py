import os
bidders_list = []
print("******* Welcome  to the Silent Auction *******")
def new_bidder(bidderlist):
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    bid = int(bid)
    bidderlist.append({ 'Name': name,
                        'Bid': bid
    })
    choice()
    return bidders_list

def choice():
    response = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if response == 'yes':
        os.system("cls")
        new_bidder(bidders_list)
    elif response == 'no':
        calculate(bidders_list)

def calculate (bidderlist):
    maxi = []
    max_var = 0
    for i in bidderlist:
        maxi.append(i.get("Bid"))
    max_var = max(maxi)
    for i in bidderlist:
        if i.get("Bid") == max_var:
            name = i.get("Name")
            print(f"The Winner of the Silent Auction is: {name}")



new_bidder(bidders_list)




