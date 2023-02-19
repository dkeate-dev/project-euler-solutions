# Copyright 2023, Dustin Keate, All rights reserved.

# Names Scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
# five-thousand first names, begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical position in the list to
# obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of
# 938 × 53 = 49714.
# What is the total of all the name scores in the file?



import string


with open("names.txt", "r") as f:
  input_line = f.readline()

names = input_line.split('","')
names[0] = names[0].replace('"', '')
names[-1] = names[-1].replace('"', '')
names = sorted(names)

result = 0
letters_dict = {}

for idx, letter in enumerate(string.ascii_uppercase):
  letters_dict[letter] = idx + 1

for idx, name in enumerate(names):
  name_score = 0
  for letter in name:
    name_score += letters_dict[letter]
  result += (idx+1) * name_score

print(result)
