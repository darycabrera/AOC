# Answer: 10624
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


possibleOutcomes = {
    (RPS.ROCK, RPS.ROCK): Result.DRAW,
    (RPS.ROCK, RPS.SCISSORS): Result.LOSS,
    (RPS.ROCK, RPS.PAPER): Result.WIN,
    (RPS.SCISSORS, RPS.ROCK): Result.WIN,
    (RPS.SCISSORS, RPS.SCISSORS): Result.DRAW,
    (RPS.SCISSORS, RPS.PAPER): Result.LOSS,
    (RPS.PAPER, RPS.ROCK): Result.LOSS,
    (RPS.PAPER, RPS.SCISSORS): Result.WIN,
    (RPS.PAPER, RPS.PAPER): Result.DRAW,
}


def to_RPS(play):
    match play:
        case "A":
            return RPS.ROCK
        case "B":
            return RPS.PAPER
        case "C":
            return RPS.SCISSORS
        case "X":
            return RPS.ROCK
        case "Y":
            return RPS.PAPER
        case _:
            return RPS.SCISSORS


def determine_result(opponent_play, my_play):
    return possibleOutcomes.get((opponent_play, my_play))


with open(sys.argv[1], "r", encoding="ascii") as fl:
    total_score = 0
    for line in fl:
        current_round = [to_RPS(play) for play in line.split()]
        my_play_score = current_round[1].value
        roundScore = determine_result(current_round[0], current_round[1]).value
        total_score += roundScore + my_play_score

    print(total_score)
