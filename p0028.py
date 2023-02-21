# Copyright 2023, Dustin Keate, All rights reserved.

# Number Spiral Diagonals

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is
# formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?



# Expand by one layer and try to figure out what is going on.

# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31

# 1 3 5 7 9   3   7   1   5     1     7     3     9
#  2 4 6 8 012 456 890 234 67890 23456 89012 45678

# Looks like the "gaps" between diagonals is the odd numbers: 1,3,5,etc, each four times.

total = 1
next_add = 1
layer = 1
increment = 2

while layer < 1001:
    for i in range(4):
        next_add += increment
        total += next_add
    layer += 2
    increment += 2

print(total)
