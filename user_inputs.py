import random


def choose_puzzle():
    puzzle_pool = ["think about it", "catchphrase", "python", "pierce the veil", "apple tree", "consciousness",
                   "Tunisia", "obsession", "fox", "tiredness", "Chicago", "chicken", "Nicholas Cage", "Aristotle",
                   "pizza", "pasta", "Palermo", "hangman", "Ferrari", "water"]
    puzzle = random.choice(puzzle_pool)
    return puzzle


def get_guess():
    guess = input(" Take a guess! ")
    return guess


def print_puzzle(puzzle, win_cons, guess):
    for w in range(0, len(puzzle[0:])):
        if puzzle[w] == guess or puzzle[w] in win_cons:
            print(puzzle[w], end="")
        elif puzzle[w] == " ":
            print(" ", end="")
        else:
            print("_", end="")
