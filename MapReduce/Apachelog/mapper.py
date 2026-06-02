#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = line.split()

    ip_address = fields[0]

    print(f"{ip_address}\t1")