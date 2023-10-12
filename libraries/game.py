from random import randint
import sys


def main():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n > 0:
                break
    guessNumber = randint(1, n)
    while True:
        try:
            guessUser = int(input("Guess: "))
            if guessUser < 0:
                continue
        except ValueError:
            pass
        else:
            if guessUser < guessNumber:
                print("Too small!")
            elif guessUser > guessNumber:
                print("Too large!")
            else:
                sys.exit("Just right!")


main()
