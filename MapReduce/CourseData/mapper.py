#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = line.split('***')

    if len(fields) < 2:
        continue

    try:
        rating = float(fields[0])

        location = fields[1]

        # Example: China_Beijing
        city_name = location.split('_', 1)[1]

        print(f"{city_name}\t{rating}")

    except (ValueError, IndexError):
        continue