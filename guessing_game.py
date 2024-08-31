import random

def guessing_game():
  """A guessing game with difficulty levels and hints."""

  difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
  if difficulty == "easy":
    range_start, range_end = 1, 20
  elif difficulty == "medium":
    range_start, range_end = 1, 50
  elif difficulty == "hard":
    range_start, range_end = 1, 100
  else:
    print("Invalid difficulty. Defaulting to easy.")
    range_start, range_end = 1, 20

  random_number = random.randint(range_start, range_end)
  attempts = 0
  hints_used = 0

  while True:
    try:
      guess = int(input(f"Guess a number between {range_start} and {range_end}: "))

      if guess < random_number:
        print("Too low!")
      elif guess > random_number:
        print("Too high!")
      else:
        attempts += 1
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        if hints_used > 0:
          print(f"You used {hints_used} hint(s).")
        break

      attempts += 1

      if attempts % 3 == 0 and hints_used < 2:
        # Generate a more relevant hint based on the random number
        if random_number % 2 == 0:
          hint = "The number is even."
        else:
          hint = "The number is odd."

        if random_number % 5 == 0:
          hint += " and a multiple of 5."

        if random_number % 10 == 0:
          hint += " and a multiple of 10."

        print(f"Hint: {hint}")
        hints_used += 1

    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  guessing_game()
