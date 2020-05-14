"""Read file into texts and calls.

Print a list of area codes and mobile prefixes called by people in Bangladore
Print the percentage of calls from fixed lines in Bangalore made to fixed lines
    also in Bangladore

Usage: Task3.py
"""

import csv

prefixes = set()
calls_from_bangladore = 0
calls_to_bangladore = 0


with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)


with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        if call[0].startswith("(080)"):
            calls_from_bangladore += 1
            if call[1].startswith("(0"):
                prefixes.add(call[1].split(")")[0][1:])
                if call[1].startswith("(080)"):
                    calls_to_bangladore += 1
            elif " " in call[1] and call[1][0] in ("7", "8", "9"):
                prefixes.add(call[1][:4])
            elif call[1].startswith("140"):
                prefixes.add(call[1][:3])

print("The numbers called by people in Bangalore have codes:")
for prefix in sorted(prefixes):
    print(prefix)

percentage = round(calls_to_bangladore / calls_from_bangladore * 100, 2)

print(
    f"{percentage} percent of calls from fixed lines in Bangalore are calls "
    "to other fixed lines in Bangalore."
)
