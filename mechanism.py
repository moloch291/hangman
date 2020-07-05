import user_inputs


def loop(puzzle):
    win_cons = []
    guesses = []
    while set(win_cons) != set(puzzle):
        guess = user_inputs.get_guess()
        guesses.append(guess)
        if guess in puzzle:
            win_cons.append(guess)
        user_inputs.print_puzzle(puzzle, win_cons, guess)
        if len(guesses) > 10:
            print("\nYou Loose!")
            quit()
    print("\nYou Win")
    quit()
