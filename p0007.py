# Copyright 2023, Dustin Keate, All rights reserved.

# 10001st Prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is
# 13.

# What is the 10,001st prime number?



# is_prime
# while iterate

nth_prime = 1
desired_prime = 10001

def is_prime(num):
  result = True
  i=1
  while result and i <= num/2 + 1:
    i+=1
    if num%i == 0 and i != num:
      result = False
  return result

for _ in range(0, desired_prime):
  i = nth_prime
  i += 1
  print(_)
  print(nth_prime)
  while not is_prime(i):
    i += 1
  nth_prime = i

print(nth_prime)

# Holy f-ing slow. Need a prime generator that stores and checks from the previously found primes
# list.
