# Copyright 2023, Dustin Keate, All rights reserved.

# Summation of Primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.



# 1. another prime generator, better than the previous
# 2. loop
# This is still crap. I need to learn Sieve of Eratosthenes, looks like. https://www.youtube.com/watch?v=JA_YrFwE1hc

import math


'''def generate_primes (max_prime):
  result = [2]

  for i in range(3,max_prime, 2):
    prime_found = True
    for j in result:
      if i%j == 0:
        prime_found = False
        break

    if prime_found:
      print(result[len(result)-1])
      result.append(i)
  
  return result'''


def sieve_of_eratosthenes(max):
  prime = [True for i in range(max + 1)]
  prime[0] = False
  prime[1] = False

  for i in range(2, math.isqrt(max)+1):
    if prime[i]:
      for j in range (i*i, max+1, i):
        prime[j] = False

  return prime


primes = sieve_of_eratosthenes(2000000)
sum_of_primes = 0

for i in range (0, len(primes)):
  if primes[i]:
    sum_of_primes += i

print(sum_of_primes)
