#!/usr/bin/env python3

import sys
import math

current_city = None
city_scores = []

def print_city_stats(city, city_scores):
    n = len(city_scores)
    avg = sum(city_scores) / n
    var = sum((s - avg) ** 2 for s in city_scores) / n
    std_dev = math.sqrt(var)
    print(f"{city}\tcount={n}\tmean={round(avg,2)}\tstd={round(std_dev,2)}")

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split('\t')
    city = parts[0]

    try:
        score = float(parts[1])
    except ValueError:
        continue

    if current_city == city:
        city_scores.append(score)
    else:
        if current_city is not None:
            print_city_stats(current_city, city_scores)
        current_city = city
        city_scores = [score]

if current_city is not None:
    print_city_stats(current_city, city_scores)