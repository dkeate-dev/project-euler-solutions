# Copyright 2023, Dustin Keate, All rights reserved.

# Largest Collatz Sequence

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
# finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.



'''a_mil = [0 for x in range(1000000)]
a_mil[1] = 1

result = []

for x in range (1, 999999):
  while a_mil[x] == 0:
    result.append(x)
    if x == 1:
      x -= 1
    elif x % 2 == 0:
      x = x // 2
    else:
      x = 3 * x + 1
  
  result = list(reversed(result))
  
  floor = a_mil[x]
  for idx, num in enumerate(result):
    a_mil[num] = floor + idx + 1'''

longest_sequence = 0
result = 0

for num in range(2, 1000000):
  x = num
  total=1
  while x != 1:
    if x % 2 == 0:
      x = x // 2
      total += 1
    else:
      x = 3 * x + 1
      total += 1
  if total > longest_sequence:
    longest_sequence = total
    result = num
    print(num)
