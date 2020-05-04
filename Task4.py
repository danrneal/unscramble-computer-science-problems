"""Read file into texts and calls.

Print list of phone numbers that could be potential telemarkers
"""

import csv

potential_telemarketers = set()


with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        potential_telemarketers.add(call[0])

    for call in calls:
        if call[1] in potential_telemarketers:
            potential_telemarketers.remove(call[1])


with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        if text[0] in potential_telemarketers:
            potential_telemarketers.remove(text[0])
        if text[1] in potential_telemarketers:
            potential_telemarketers.remove(text[1])

print("These numbers could be telemarketers:")
for potential_telemarketer in sorted(potential_telemarketers):
    print(potential_telemarketer)
