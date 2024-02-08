# Answer: 14060
from enum import Enum
import sys


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


plays = {
    (RPS.ROCK, Result.DRAW): RPS.ROCK,
    (RPS.ROCK, Result.LOSS): RPS.SCISSORS,
    (RPS.ROCK, Result.WIN): RPS.PAPER,
    (RPS.PAPER, Result.LOSS): RPS.ROCK,
    (RPS.PAPER, Result.WIN): RPS.SCISSORS,
    (RPS.PAPER, Result.DRAW): RPS.PAPER,
    (RPS.SCISSORS, Result.WIN): RPS.ROCK,
    (RPS.SCISSORS, Result.DRAW): RPS.SCISSORS,
    (RPS.SCISSORS, Result.LOSS): RPS.PAPER,
}


def to_RPS(play):
    match play:
        case "A":
            return RPS.ROCK
        case "B":
            return RPS.PAPER
        case _:
            return RPS.SCISSORS


def to_result(result):
    match result:
        case "X":
            return Result.LOSS
        case "Y":
            return Result.DRAW
        case _:
            return Result.WIN


def determine_play(opponent_play, result):
    return plays.get((opponent_play, result))


with open(sys.argv[1], "r", encoding="ascii") as fl:
    total_score = 0
    for line in fl:
        current_round = line.split()
        elf_play = to_RPS(current_round[0])
        expected_result = to_result(current_round[1])
        my_play = determine_play(elf_play, expected_result)
        total_score += expected_result.value + my_play.value

    print(total_score)
