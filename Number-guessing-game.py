import random

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("choose a difficulty. Type 'easy' or 'hard' : ")
num = random.randint(0, 100)

def checkit(the_num, the_guess):
  if the_num == the_guess:
    print(f"You got it the answer is {the_guess}.")
    return True
  elif the_num < the_guess:
    print("Too high.")
  elif the_num > the_guess:
    print("Too low.")
repeat = 'y'
while repeat == 'y':
  if difficulty == 'easy':
    for i in range(10, 0, -1):
      print(f"You have {i} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if checkit(num, guess):
        break
      if i == 1:
        print("You've run out of guesses, you lose.")
        break
      print("Guess again.")
  elif difficulty == 'hard':
    for i in range(5, 0, -1):
      print(f"You have {i} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if checkit(num, guess):
        break
      if i == 1:
        print("You've run out of guesses, you lose.")
        break
      print("Guess again.")
  repeat = input("You want to play again? 'y' or 'n'.")
    