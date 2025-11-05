import re

"""
given the lines in the calibration document,
for each line, find the first and last number,
written out numbers are considered digits,
combine them into a two-digit integer,
and sum all the integers together to get the final result
"""

def written_number_to_digit(s: str) -> str:
    """
    Helper func to convert written numbers if needed
    if it's already a digit, just return it
    """
    written_to_digit = {
        'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine': '9'
    }

    # convert written numbers to digits
    if s in written_to_digit:
        s = written_to_digit[s]

    return s

# open file in ./input folder and get lines
with open('./input/calibration_document.txt') as f:
    lines = f.readlines()

# for each line regex out each numerical character and combine to an int
results = []
for line in lines:
    nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    if nums:
        first = nums[0]
        last = nums[-1]

        # normalize written numbers if needed
        first = written_number_to_digit(first)
        last = written_number_to_digit(last)

        # combine to an int and add to results
        combined = int(first + last)
        results.append(combined)

# once done add up all the ints in the list
total = sum(results)

# print our result
print(total)