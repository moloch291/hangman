import mechanism
import user_inputs


def main():
    print("Hi! It's a hangman game! Let's test your skills! \n Watch out for capital letters!")
    game()


def game():
    puzzle = user_inputs.choose_puzzle()
    mechanism.loop(puzzle)
    print("Good Bye!")


if __name__ == '__main__':
    main()
