# Copyright 2023, Dustin Keate, All rights reserved.

# Amicable Numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
# into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are
# called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
# d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.



# TODO: make a list of divisors, sum them (store in a dict?)
# TODO: find amicable numbers in the dict

dict = {}
temp_divisors = []
dict['1'] = 0

for i in range(2, 10001):
  for j in range(1, i//2+1):
    if i%j == 0:
      temp_divisors.append(j)
  dict[f"{i}"] = sum(temp_divisors)
  temp_divisors = []

# I can probably go through the list once only, but...

result = 0
temp_sum = 0

for i in range(2, 10001):
  if dict[f"{i}"] <= 10000:
    if dict[f"{dict[f'{i}']}"] == i and dict[f"{i}"] != i:
      result += i
      print(i)
  else: # if a divisor sum is above 10k, check if it is amicable
    temp_divisors = []
    for j in range(1, i//2+1):
      if i%j == 0:
        temp_divisors.append(j)
    temp_sum = sum(temp_divisors)
    temp_divisors = []
    for k in range(1, temp_sum//2+1):
      if temp_sum%k == 0:
        temp_divisors.append(k)
    if dict[f"{i}"] == sum(temp_divisors):
      result += i
      print(i)
    temp_sum = 0

print(result)

#thwarted by 6 and 28 because they are not amicable to anybody, but themselves, which is not technically amicable.
