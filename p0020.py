# Copyright 2023, Dustin Keate, All rights reserved.

# Factorial Digit Sum

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!



result = 1

for i in range(100, 0, -1):
  result *= i

print(result)

answer = 0

for letter in str(result):
  answer += int(letter)

print(answer)
