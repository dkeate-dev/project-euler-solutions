# Copyright 2023, Dustin Keate, All rights reserved.

# Largest Palindrome Project

# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.



# What's the best order? Find palindromes and factorize or check if multiples are palindromes
# Iterate from the top? 
# 999 x 999, 
# 999 x 998, 
# 998 x 998, 
# 999 x 997, 
# 998 x 997, ...

def reversed(forwards):
  backwards = []
  forwards_length = len(forwards) 

  for i in range(1, forwards_length + 1):
    backwards.append(forwards[forwards_length-i])

  return "".join(backwards)

def is_palindrome(forwards):
  return str(forwards) == reversed(forwards) 

result_found = False
result = 0
x = 999
y = 999

while (not result_found) and x > 0:
  while (not result_found) and y >= x:
    if is_palindrome(str(x*y)):
      print(x*y)
      print(x)
      print(y)
    
    y -= 1
  x -= 1
  y = 999

# Wound up dumping the result_found sentinel variable as the two greatest numbers is not necessarily the solution. 993 x 913 > 924 x 962
