import os

print("Welcome to the secret auction program.")
bid_dict = {}
bids = True

def bid():
    bidder_input = input("What is your name:bid?\n")
    bidder, amount = bidder_input.split(":", 1)
    bid_dict[bidder.strip().lower()] = int(amount.strip())
    new_bid = input("Are there more bidders 'Y/y' for Yes or 'N/n' for No? ").lower()
    if new_bid == "y":
        return True, bid_dict
    else:
        return False, bid_dict
        
while bids:
    bids, bid_dict = bid()

print(bid_dict)
winning_bidder = max(bid_dict, key=bid_dict.get)
winning_bid = bid_dict[winning_bidder]
print(f"The winning bid is ${winning_bid} by {winning_bidder}")