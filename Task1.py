"""Read file into texts and calls.

Print the number of unique telephone numbers in the records

Usage: Task1.py
"""

import csv

numbers = set()


with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        numbers.add(text[0])
        numbers.add(text[1])


with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        numbers.add(call[0])
        numbers.add(call[1])


print(f"There are {len(numbers)} different telephone numbers in the records.")
