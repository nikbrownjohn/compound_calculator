#!/usr/bin/env python3

# Asking user for input
trades_0 = 0
trades = int(input("How Many Trades To Forecast Compound Statistics?: "))
balance = int(input("What is Your Account Balance?: "))
risk_reward_ratio = int(input("Average Risk Reward?: "))
risk = int(input("Risk Percentage?: "))
counter = 0

# Calculate compound forecast
for i in range(trades_0, trades):
	new_balance = (balance * risk/100)
	new = new_balance * risk_reward_ratio
	balance += new
	counter += 1
	print("Trade","{}".format(counter),")", "{:,}".format(balance))

# Forecast for compound is working nicely, 
# although win rate must be factored in. 
# Amendments will be made
