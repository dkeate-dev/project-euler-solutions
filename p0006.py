# Copyright 2023, Dustin Keate, All rights reserved.

# Sum Square Difference

# The sum of the squares of the first ten natural numbers is
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the
# square of the sum is
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and
# the square of the sum.



def sum_of_squares(num):
  result = 0
  for i in range(1, num+1):
    result += i*i
  return result

def square_of_sums(num):
  result = 0
  for i in range(1, num+1):
    result += i
  return result*result

print(sum_of_squares(100)-square_of_sums(100))
