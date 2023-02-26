# Code is Copyright 2023, Dustin Keate, All rights reserved.



# The following problem is taken from Project Euler.

# Coin Sums

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins
# in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?



# Nested loops from hell is an option. There's probably a recursion option as well.

COINS = (100,50,20,10,5,2,1) # Ignore 200p and just add 1 to the answer.
MAX = 200

def do_the_thing(denom, value, count):
    if denom >= len(COINS):
        return count

    while value < MAX:
        count = do_the_thing(denom + 1, value, count)
        value += COINS[denom]
    
    if value == MAX:
        return count + 1
    else:
        return count

print(do_the_thing(0, 0, 0))