# Code is Copyright 2023, Dustin Keate, All rights reserved.



# The following problem is taken from Project Euler.

# Pandigital Products

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
# exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
# multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1
# through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in
# your sum.



# DOESN'T INCLUDE ZERO. READ THAT AGAIN.
# A 3 digit times 3 digit number is at a minimum 5 digits, so impossible.
# 99 * 99 is 4 digits, so impossible again.
# All values must be xx * xxx
# WRONG! x * xxxx is also possible!

DIGITS = [x for x in range(1,10)]

# First, let's learn about list equality

print(DIGITS)
print(DIGITS == [1,2,3,4,5,6,7,8,9])
print(DIGITS == [1,2,3,4,5,6,7,9,8]) # Must be in same order.
print([1,2,3,4,5,6,7,9,8].sort()) # Interesting...
tester = [1,2,3,4,5,6,7,9,8]
tester.sort()
print(DIGITS == tester)
tester.append(9)
print(DIGITS == tester)

# Seems to me like they work exactly like I would expect them to.
# Now, start multiplying and checking, abusing strings.

result = []

for a in range(1,100):
    for b in range(100,10000):
        product = a * b
        equation_digits = str(product) + str(a) + str(b)
        equation_list = []
        for letter in equation_digits:
            equation_list.append(int(letter))
        equation_list.sort()
        if equation_list == DIGITS:
            print(f"{a} * {b} = {product}")
            result.append(product)

result = set(result) # Remove duplicates, dummy!

answer = 0

for i in result:
    answer += i

print(result)
print(answer)
