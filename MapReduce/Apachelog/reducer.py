#!/usr/bin/env python3

import sys

current_ip = None
total_hits = 0

for line in sys.stdin:

    line = line.strip()

    ip_address, hit_count = line.split('\t', 1)

    try:
        hit_count = int(hit_count)
    except ValueError:
        continue

    if current_ip == ip_address:
        total_hits += hit_count
    else:
        if current_ip:
            print(f"{current_ip}\t{total_hits}")

        current_ip = ip_address
        total_hits = hit_count

if current_ip == ip_address:
    print(f"{current_ip}\t{total_hits}")