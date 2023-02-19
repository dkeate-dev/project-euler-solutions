# Copyright 2023, Dustin Keate, All rights reserved.

# Smallest Multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
# remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



# Options appear to factorize 1 through 20 and multiply
# or brute force from 2520 * 11 * 13 * 17 * 19
# (this may be the answer) (Add a 2 for 16?) (This is a coding problem, not math)
# Facrorization may have a problem with duplicates, e.g. 4 is two 2s

def prime_factorization(num):
  factors = []
  for i in range (2,(int(num/2+2))):
    while num%i == 0:
      factors.append(i)
      num = int(num/i)

  return(factors)

print(prime_factorization(2520))

print(2520*11*13*17*19*2) 

# at least I wrote a prime_factorization function before cheating
