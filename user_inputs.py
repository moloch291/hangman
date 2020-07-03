def get_user_inputs(puzzle):
    guess = input(" Take a guess! ")
    for c in range(0, len(puzzle)):
        if puzzle[c] == guess:
            print(puzzle[c], end="")
        elif puzzle[c] == " ":
            print(" ", end="")
        else:
            print("_", end="")