print("Welcome to the secret auction program.")
bid_dict = {}
bids = True

def bid():
    bidder_input = input("What is your name:bid?\n")
    bidder, amount = bidder_input.split(":", 1)
    bid_dict[bidder.strip()] = amount.strip()
    new_bid = input("Are there more bidders 'Y/y' for Yes or 'N/n' for No? ").lower()
    if new_bid == "y":
        print(new_bid)
        return bid_dict, bids
    else:
        print(new_bid)
        bids = False
        return bids, bid_dict
        
while bids != False:
    bids, bid_dict = bid()
