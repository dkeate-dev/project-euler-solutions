# Copyright 2023, Dustin Keate, All rights reserved.

# Sieve or Eratosthenes returns a list of primes below a given value.


def sieve(max : int) -> [int]:
    test_list = [True for i in range(max + 1)]
    test_list[0] = False
    test_list[1] = False

    primes = []
    
    highest_index = len(test_list) - 1
    next_check = 2
    multiplier = 2
    next_non_prime = multiplier * next_check

    while next_check <= highest_index:
        if test_list[next_check]:
            primes.append(next_check)
            while next_non_prime <= highest_index:
                test_list[next_non_prime] = False
                multiplier += 1
                next_non_prime = multiplier * next_check
        next_check += 1
        multiplier = 2
        next_non_prime = multiplier * next_check

    return primes
