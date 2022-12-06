import os

from get_input import request_input

SESSION = os.environ.get("SESSION", "")

input = request_input(4, SESSION)


def split_str(string: str, sep: str) -> list[str]:
    return string.split(sep)


# part 1
overlaps = 0
for pair in input.split("\n")[:-1]:
    interval_1, interval_2 = [
        split_str(interval, "-") for interval in split_str(pair, ",")
    ]

    if (int(interval_1[0]) <= int(interval_2[0])) and (
        int(interval_1[1]) >= int(interval_2[1])
    ):
        overlaps += 1
    elif (int(interval_2[0]) <= int(interval_1[0])) and (
        int(interval_2[1]) >= int(interval_1[1])
    ):
        overlaps += 1

# part 2
overlaps = 0
for pair in input.split("\n")[:-1]:
    interval_1, interval_2 = [
        split_str(interval, "-") for interval in split_str(pair, ",")
    ]

    if (int(interval_1[1]) >= int(interval_2[0])) and (
        int(interval_1[0]) <= int(interval_2[0])
    ):
        overlaps += 1
    elif (int(interval_2[1]) >= int(interval_1[0])) and (
        int(interval_2[0]) <= int(interval_1[0])
    ):
        overlaps += 1
