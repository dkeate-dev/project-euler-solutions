# Code is Copyright 2023, Dustin Keate, All rights reserved.



# The following problem is taken from Project Euler.

# Digit Cancelling Fractions

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
# simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling
# the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and
# containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the
# denominator.



# Seems straight forward. 
# Nested loops and nested if statements...

from fractions import Fraction


answers = []

for n in range(11,100):
    for d in range(11,100):
        result = True
        f_begin = Fraction(n,d)
        numerator = [digit for digit in str(n)]
        denominator = [digit for digit in str(d)]
        if n >= d or n%10 == 0 or d%10 == 0:
            result = False
        else:
            if numerator[1] == denominator[0]:
                numerator.pop(1)
                denominator.pop(0)
            elif numerator[0] == denominator[1]:
                numerator.pop(0)
                denominator.pop(1)
            else:
                result = False
        if result:
            f_end = Fraction(int(numerator[0]), int(denominator[0]))
            if f_end == f_begin:
                answers.append((n,d))

print(answers)

final_answer = 1

for values in answers:
    final_answer *= Fraction(values[0], values[1])

print(final_answer)
