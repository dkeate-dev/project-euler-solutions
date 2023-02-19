# Copyright 2023, Dustin Keate, All rights reserved.

# Lexicographic Permutations

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
# of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?



# TODO: This is probably recursion? Still bad at recursion!
# TODO: Number of permutations = n!. 10! = 3,628,800
# TODO: Maybe a series of swaps?
# TODO: Maybe I can generate the list and then sort it? This is probably cheating.
# TODO: Pop one value starting at the beginning. Pass remaining (still sorted) string to recursive function. OH HAI, THE ANSWER.


def permute (results_list, result_str, rem_str):
  if rem_str == "":
    results_list.append(result_str)
    return
  
  for idx, char in enumerate(rem_str):
    permute(results_list, result_str + char, rem_str[:idx] + rem_str[(idx+1):])


working_str = "0123456789"
result = []
permute(result, "", working_str)
result = sorted(result)
print(result[1000000-1])
