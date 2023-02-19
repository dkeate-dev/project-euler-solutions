# Copyright 2023, Dustin Keate, All rights reserved.

# Non-abundant Sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the
# number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
# means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called
# abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
# all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
# upper limit cannot be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant
# numbers.



abundant_numbers = []
divisors = []

for i in range(1, 28124):
  for j in range(1, i//2+1):
    if i%j == 0:
      divisors.append(j)
  if sum(divisors) > i:
    print(i)
    abundant_numbers.append(i)
  divisors = []

abundant_sum = [False for i in range(0,28124)]

for i in abundant_numbers:
  print(i)
  for j in abundant_numbers:
    if i+j < 28124:
      abundant_sum[i+j] = True

answer = 0

for index, val in enumerate(abundant_sum):
  if not val:
    answer += index

print(answer)

# TODO: I need to learn a better and more efficient way of generating divisors.
# TODO: Also, line 26 companion else should break out of each line 25 loop when it exceeds the max
# value. Can I do that in Python?
