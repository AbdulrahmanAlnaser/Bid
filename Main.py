bids = {} 

bidder_end = "yes"
while bidder_end == "yes":
    bidder_name = input("What is your name? ").title()
    offer = float(input("What is your proposed bid? $"))
    
   
    if bidder_name in bids:
        bids[bidder_name].append(offer)  
    else:
        bids[bidder_name] = [offer]  
    
    bidder_end = input("Are there any other bidders? (yes or no): ")

max_offer = 0
max_bidder = ""
print("\nBidders and their respective offers:")
for bidder, offers in bids.items():
    print(f"{bidder}: {offers}")
    if max(offers) > max_offer:
        max_offer = max(offers)
        max_bidder = bidder

print(f"\nThe winner is  ${max_bidder} with bid of {max_offer}.")
