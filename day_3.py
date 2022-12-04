import os
import re

from get_input import request_input

SESSION = os.environ.get("SESSION", "")

input = request_input(3, SESSION)

items = []
for string in input.split('\n')[:-1]:
    mid = int(len(string)/2)
    item = re.search(f"[{string[:mid]}]", string[mid:]).group(0)
    items.append(item)

scores = 'abcdefghijklmnopqrstuvwxyz'

priorities_sum = 0
for item in items:
    if item in scores:
        priorities_sum += scores.index(item) + 1
    else:
        priorities_sum += scores.upper().index(item) + 27
