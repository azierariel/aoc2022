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


def calc_priorities(items: list[str]) -> int:
    scores = 'abcdefghijklmnopqrstuvwxyz'
    priorities_sum = 0
    for item in items:
        if item in scores:
            priorities_sum += scores.index(item) + 1
        else:
            priorities_sum += scores.upper().index(item) + 27
    return priorities_sum


### part 2
sacks = input.split('\n')[:-1]
items = []
sacks_n = len(sacks)
for i in range(0,sacks_n,3):
    string = '@'.join(sacks[i:i+3])
    
    item = re.search(r"(.).*@.*(\1).*@.*(\1)", string).group(1)
    items.append(item)

priorities = calc_priorities(items)
