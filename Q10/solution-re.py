# http://www.pythonchallenge.com/pc/return/bull.html

import re

n = 30
sequence = "1"

for _ in range(n):
    next_sequence = ""
    for match in re.finditer(r"(\d)\1*", sequence):
        count = len(match.group())
        digit = match.group()[0]
        next_sequence += str(count) + digit
    sequence = next_sequence

print(len(sequence))
