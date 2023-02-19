# Copyright 2023, Dustin Keate, All rights reserved.

# Power Digit Sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?



start = pow(2, 1000)

num_list = [int(num) for num in str(start)]

result = 0

for num in num_list:
  result += int(num)

print(result)
