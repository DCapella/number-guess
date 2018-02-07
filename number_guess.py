import random
import sys

def main(name):
    count = 1
    answer = random.randint(1, 20)

    print("Well, " + name + ", I am thinking of a number between 1 and 20.")

    for count in range(6):
        guess = int(input("Take a guess.\n>> "))

        if guess == answer:
            print(f"Good job, %s! You guessed my number in %i guesses!" % (name, (count + 1)))
            return play_again(name)
        if guess > answer:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    print("Nope. The number I was thinking of was " + str(answer) + ".")
    return play_again(name)

def play_again(name):
    play_again = input("Do you want to play again? y/n\n>> ")

    if play_again.lower() == 'y':
        return main(name)
    else:
        sys.exit(0)


name = input("Hello, what is your name?\n>> ")
main(name)
