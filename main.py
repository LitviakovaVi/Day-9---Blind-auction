from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False #условие для цикла

def find_highest_bidder(bidding_record):
  highest_bid = 0 #начальная ставка = 0
  winner = "" 
  # bidding_record = {"Angela": 123, "James": 321}
  # ищем максимальную ставку:
  for bidder in bidding_record: 
    bid_amount = bidding_record[bidder] #новая ставка =
    if bid_amount > highest_bid: # если новая ставка выше предыдущей, максимальная ставка = новой ставке
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price # записываем в словарь ключ и значение
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
  

