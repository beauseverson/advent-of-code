import re

"""
given the lines in the calibration document,
for each line, find the first and last numerical character,
combine them into a two-digit integer,
and sum all the integers together to get the final result
"""

# open file in ./input folder and get lines
with open('./input/calibration_document.txt') as f:
    lines = f.readlines()

# for each line regex out each numerical character and combine to an int
results = []
for line in lines:
    nums = re.findall(r'\d', line)
    if nums:
        first = nums[0]
        last = nums[-1]
        combined = int(first + last)
        results.append(combined)

# once done add up all the ints in the list
total = sum(results)

# print our result
print(total)