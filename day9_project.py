import os

print("Welcome to the secret auction program.")
bid_dict = {}
bids = True

def bid():
    bidder_input = input("What is your name:bid?\n")
    bidder, amount = bidder_input.split(":", 1)
    bid_dict[bidder.strip()] = amount.strip()
    new_bid = input("Are there more bidders 'Y/y' for Yes or 'N/n' for No? ").lower()
    if new_bid == "y":
        return bids, bid_dict
    else:
        print(new_bid)
        bids = False
        return bids, bid_dict
        
while bids:
    bids, bid_dict = bid()

winning_bidder = max(bid_dict, key=bid_dict.get)
winning_bid = bid_dict[winning_bidder]
print(f"The winnin bid is {winning_bid} by {winning_bidder}")