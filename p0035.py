# Code is Copyright 2023, Dustin Keate, All rights reserved.



# The following problem is taken from Project Euler.

# Circular Primes

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and
# 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?



from reusable.sieve import sieve


def check_circular(num, primes):
    next_num = num

    while next_num in primes:
        num_str = [a for a in str(next_num)]
        temp_char = num_str.pop(-1)
        num_str.insert(0, temp_char)
        new = ""
        for l in num_str:
            new += l
        next_num = int(new)
        if next_num == num:
            return True
    
    return False


primes = sieve(1000000)

result = []

for val in primes:
    if (check_circular(val, primes)):
        result.append(val)

print(result)

# check_circular should probably be looped using math instead of weird string manipulation
