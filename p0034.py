# Code is Copyright 2023, Dustin Keate, All rights reserved.



# The following problem is taken from Project Euler.

# Digit Factorials

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.



# Simple?

# sum_fac(9,999,999) = 2,540,160. This is a (bad) maximum.

from math import factorial


def sum_fac(num):
    result = 0
    for digit in str(num):
        result += factorial(int(digit))
    return result

ans = []

for num in range(3,2540161):
    fac = sum_fac(num)
    if num == fac:
        ans.append(num)
        print(num)

print(sum(ans))
