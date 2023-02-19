# Copyright 2023, Dustin Keate, All rights reserved.

# Largest Prime Factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?



result = 1
x = 600851475143
test_factor = 2

while (x != 1):
  if (x%test_factor == 0):
    print(test_factor)
    x = int(x/test_factor)
    if test_factor > result:
      result = test_factor
  test_factor += 1
