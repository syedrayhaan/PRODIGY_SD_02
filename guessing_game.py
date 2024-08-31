import random

def guessing_game():
  """A guessing game where the user tries to guess a random number."""

  random_number = random.randint(1, 100)
  attempts = 0

  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))

      if guess < random_number:
        print("Too low!")
      elif guess > random_number:
        print("Too high!")
      else:
        attempts += 1
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

      attempts += 1
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  guessing_game()