bids={}
bidding_finished=False

def highest_bid(bidding_price) :
    bid_Amount=0
    highest_Amount=0
    for user in bidding_price :
        bid_Amount=int(bidding_price[user])
        if bid_Amount>highest_Amount :
            highest_Amount=bid_Amount
            won=user
    print(f"{user} Won the Amount $ : {highest_Amount}")

while not bidding_finished :
    name=input("Enter your name :")
    price=input("What is your bid : $")
    bids[name]= price
    do_continue=input("Continue yes or no :")
    if do_continue=="no" :
        bidding_finished=True
        highest_bid(bids)
        

  
