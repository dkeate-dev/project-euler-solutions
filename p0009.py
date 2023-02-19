# Copyright 2023, Dustin Keate, All rights reserved.

# Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.



# 1. check if a sqare root is an integer
# 2. generate triplets?
# 3. ...until one meets the requirements

import math


def is_sqrt_int(num):
  return math.isqrt(num) ** 2 == num


def generate_triplets(max_b):
  result = []
  b = 1

  while b < max_b:
    for a in range (1, b+1):
      if is_sqrt_int(a**2 + b**2):
        result.append([a, b, math.isqrt(a**2 + b**2)])
    b += 1

  return result


triplets = generate_triplets(500)

for i in range(len(triplets)):
  if triplets[i][0]+ triplets[i][1] + triplets[i][2] == 1000:
    print(triplets[i])

# manually multiplied
