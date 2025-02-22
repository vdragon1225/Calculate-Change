'''
Author: Daniel Lai
Date: 2/21/25
File: CalculateChange.py
  
'''

# Prompt user for input
print("Enter the number of cents: ")
numCents = int(input()) 

# Calculate the number of coins
quarters = numCents // 25 # calculate number of quarters
numCents %= 25 # calculate remainder of cents

dimes = numCents // 10 # calculate number of dimes
numCents %= 10 # calculate remainder of cents

nickels = numCents // 5 # calculate number of nickels
numCents %= 5 # calculate remainder of cents

pennies = numCents # set pennies equal to remainder of cents

# Output and format the results
print(f"{'Quarters:':<10}{quarters:>8}")
print(f"{'Dimes:':<10}{dimes:>8}")
print(f"{'Nickels:':<10}{nickels:>8}")
print(f"{'Pennies:':<10}{pennies:>8}")