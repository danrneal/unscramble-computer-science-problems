"""Read file into texts and calls.

Print the first record of texts and the last record of calls

Usage: Task0.py
"""

import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)
    incoming_number, answering_number, time = texts[0]

    print(
        f"First record of texts, {incoming_number} texts {answering_number} "
        f"at time {time}"
    )


with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)
    incoming_number, answering_number, time, duration = calls[-1]

    print(
        f"Last record of calls, {incoming_number} calls {answering_number} at "
        f"time {time}, lasting {duration} seconds"
    )
