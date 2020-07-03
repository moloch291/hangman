import random


def choose_puzzle():
    puzzle_pool = ["think about it", "catchphrase", "python", "pierce the veil", "apple tree", "consciousness",
                   "Tunisia", "obsession", "fox", "tiredness", "Chicago", "chicken", "Nicholas Cage", "Aristotle",
                   "pizza", "pasta", "Palermo", "hangman", "Ferrari", "water"]
    puzzle = random.choice(puzzle_pool)
    return puzzle


def hide_puzzle(puzzle):
    for c in range(0, len(puzzle)):
        if puzzle[c] == " ":
            print(" ", end="")
        else:
            print("_", end="")
    return puzzle


def get_guesses(puzzle):
    for i in range(0, 10):
        guess = input(" Take a guess! ")
        for w in range(0, len(puzzle)):
            if puzzle[w] == guess:
                print(puzzle[w], end="")
            elif puzzle[w] == " ":
                print(" ", end="")
            else:
                print("_", end="")
