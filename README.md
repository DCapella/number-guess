# Number Guess

Number Guess is a Python 3 based gamed whereas the opponent will think of a number from 1 - 20 and you have 6 tries with hints such as too high or too low.

# How to run it

Number Guess is ran through command line. When you're in '../../number-guess' just enter 'Python3 number_guess.py' and start playing!

# Break Down

The first part is asking for your name with a simple input line:
  `input("Hello, what is your name?\n>> ")` and storing that answer in a String variable name.
  Afterwards, it automatically continues on to `main()`.

It then goes on to ask you to make your first guess looped until your 6th guess:
  ```python
  for count in range(6):
        guess = int(input("Take a guess.\n>> "))
  ```

It will tell you if you guess too high:
  ```python
  if guess > answer:
          print("Your guess is too high.")
  ```
Or too low:
  ```python
else:
        print("Your guess is too low.")
  ```

If you answer right,
  `print(f"Good job, %s! You guessed my number in %i guesses!" % (name, (count + 1)))`, or wrong, `print("Nope. The number I was thinking of was " + str(answer) + ".")`, it will always ask you if you want to play again with a function:
  ```python
  def play_again(name):
      play_again = input("Do you want to play again? y/n\n>> ")

      if play_again.lower() == 'y':
          return main(name)
      else:
          sys.exit(0)
  ```
