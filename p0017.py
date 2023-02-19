# Copyright 2023, Dustin Keate, All rights reserved.

# Number Letter Counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
# letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
# letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.



ones = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}


def to_words(number):
  result = ""
  if number > 99:
    result += ones[number//100] + "hundred"
    number = number % 100
    if number > 0:
      result += "and"
  if number < 20:
    if number > 0:
      result += ones[number]
  else:
    result += tens[number//10]
    number = number % 10
    if number > 0:
      result += ones[number]
  if result == "tenhundred":
    result = "onethousand"
  return result


answer = 0

for num in range(1, 1001):
  answer += len(to_words(num))

print(answer)
