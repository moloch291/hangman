import random


def choose_puzzle():
    puzzle_pool = ["think about it", "catchphrase", "python", "pierce the veil", "apple tree", "consciousness",
                   "Tunisia", "obsession", "fox", "tiredness", "Chicago", "chicken", "Nicholas Cage", "Aristotle",
                   "pizza", "pasta", "Palermo", "hangman", "Ferrari", "water"]
    puzzle = random.choice(puzzle_pool)
    return puzzle


def get_guesses(puzzle):
    win_cons = []
    mistakes = []
    for i in range(0, 16):
        guess = input(" Take a guess! ")
        for w in range(0, len(puzzle[0:])):
            if puzzle[w] == guess or puzzle[w] in win_cons:
                print(puzzle[w], end="")
            elif puzzle[w] == " ":
                print(" ", end="")
            else:
                print("_", end="")
        if guess in puzzle:
            win_cons.append(guess)
        else:
            mistakes.append(guess)
