# Copyright 2023, Dustin Keate, All rights reserved.

# Digit Fifth Powers

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of
# their digits:

# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.



# 9**4 * 5 = 32805. Logically, this a hard maximum for the problem worth checking.

# Loop up to 9**5 * 6 = 354294, an option for hard maximum. There is a better option for sure.

def check_pow_sum(power, num):
    digit_list = [int(char) for char in str(num)]
    result = 0
    for i in digit_list:
        result += i**power
    return num == result

answer = []

for i in range(1,354295):
    if check_pow_sum(5, i):
        answer.append(i)

print(sum(answer))

# Subtract 1 because I am an idiot.
