# Copyright 2023, Dustin Keate, All rights reserved.

# Reciprocal Cycles

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
# with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
# 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
# fraction part.



# TODO: Append remainders (starting with 1) and keep going until one repeats. count back.

def find_recurring(denominator):
    numerator = 1
    remainders = []

    while numerator != 0 and numerator not in remainders:
        remainders.append(numerator)
        numerator = numerator * 10 % denominator

    if numerator == 0:
        return 0
    else:
        return len(remainders) - remainders.index(numerator)

result = 0
result_length = 0

for i in range(1,1000):
    temp = find_recurring(i)
    if temp > result_length:
        result = i
        result_length = temp

print(result, result_length)
