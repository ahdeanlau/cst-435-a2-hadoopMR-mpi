#!/usr/bin/python
# The Reducer
import sys
from collections import defaultdict

# Initialize a dictionary to store counts
counts = defaultdict(int)
# Read input from stdin
for line in sys.stdin:
    try:
        # Parse the input line
        key, count = line.strip().rsplit(" - ", 1)
        counts[key] += int(count)
    except Exception as e:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)
        sys.exit(0)

# # Output the aggregated results
for key in sorted(counts):
    print(key+" = "+str(counts[key]))
