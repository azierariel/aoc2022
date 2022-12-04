import os
from get_input import request_input

SESSION = os.environ.get("SESSION", "")

# A: Rock, B: Paper, C: Scissors
# X: Rock, Y: Paper, Z: Scissors


def round_result(round: str) -> int:
    me = round.split(" ")[1]
    opponent = round.split(" ")[0]
    shape_score = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    if shape_score[me] == shape_score[opponent]:
        return 3 + shape_score[me]
    if me == "X" and opponent == "C":
        return 6 + 1
    if me == "Y" and opponent == "A":
        return 6 + 2
    if me == "Z" and opponent == "B":
        return 6 + 3
    else:
        return 0 + shape_score[me]


def follow_strategy(round: str) -> int:
    me = round.split(" ")[1]
    opponent = round.split(" ")[0]
    # Rules: given a figure (A B C)
    # , pos(0) wins against given figure
    # , pos(1) lose against given figure
    # , pos(2) draw against given figure
    rules = {"A": ["Y", "Z", "X"], "B": ["Z", "X", "Y"], "C": ["X", "Y", "Z"]}
    me_plays = rules[opponent]
    if me == "X":  # lose
        round = f"{opponent} {me_plays[1]}"
        return round_result(round)
    if me == "Z":  # win
        round = f"{opponent} {me_plays[0]}"
        return round_result(round)
    else:  # draw
        round = f"{opponent} {me_plays[2]}"
        return round_result(round)


input = request_input(2, SESSION)

# first puzzle
score = 0
for round in input.split("\n")[:-1]:
    score += round_result(round)

# 2dn puzzle
score = 0
for round in input.split("\n")[:-1]:
    score += follow_strategy(round)
