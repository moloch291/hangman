import random
from user_inputs import *


def main():
    print("Hi, this is a hangman game. Let's test your skills!")


def choose_puzzle():
    puzzle_pool = ["think about it", "catchphrase", "python", "pierce the veil", "apple tree", "consciousness",
                   "Tunisia", "obsession", "fox", "tiredness", "Chicago", "chicken", "Nicholas Cage", "Aristotle",
                   "pizza", "pasta", "Palermo", "hangman", "Ferrari", "water"]
    puzzle = random.choice(puzzle_pool)
    print(puzzle)
    return puzzle


get_user_inputs(choose_puzzle())
