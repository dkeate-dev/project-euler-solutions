# Code is Copyright 2023, Dustin Keate, All rights reserved.



# The following problem is taken from Project Euler.

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously
# remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly
# we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to
# left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.



from reusable.sieve import sieve

primes = sieve(1000000)

def check_trunctable_bidirectional (candidate):
    sentinel = True

    for i in range(1,len(str(candidate))):
        if int(str(candidate)[:i]) not in primes:
            sentinel = False
            break
        if int(str(candidate)[i:]) not in primes:
            sentinel = False
            break
    
    return sentinel

solution = []

for num in primes:
    if check_trunctable_bidirectional (num):
        solution.append(num)
        print(num)

print (sum(solution) - 17) # -17 to get rid of 2,3,5,7 and I'm lazy

# why is the last one so high? it takes forever.
