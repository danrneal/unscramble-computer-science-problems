"""Read file into texts and calls.

Print the phone number that spent to longest time on the phone

Usage: Task2.py
"""

import csv

durations = {}
phone_number = None


with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        durations[call[0]] = durations.get(call[0], 0) + int(call[3])
        durations[call[1]] = durations.get(call[1], 0) + int(call[3])


for number in durations:
    if phone_number is None or durations[number] > durations[phone_number]:
        phone_number = number

# phone_number = max(durations, key=durations.get)  # Might not be allowed


print(
    f"{phone_number} spent the longest time, {durations[phone_number]} "
    "seconds, on the phone during September 2016."
)
