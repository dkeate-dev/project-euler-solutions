# Code is Copyright 2023, Dustin Keate, All rights reserved.



# The following problem is taken from Project Euler.

# Double-base Palindromes

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)



solutions = []

def check_palindrome (candidate):
    return (candidate == candidate[::-1])


for i in range(1000000):
    if i % 10 != 0:
        if check_palindrome(str(i)):
            if check_palindrome(str(bin(i)[2:])):
                solutions.append(i)

print(sum(solutions))
