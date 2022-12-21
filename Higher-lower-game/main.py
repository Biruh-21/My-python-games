import art
import game_data
import os
import random

def who_has_more_follower(A, B, answer):
  """
  This function receives two dictionaries
  as an argument and tells who has more follower.
  """
  win = False
  A_follower = A['follower_count']
  B_follower = B['follower_count']
  if answer == 'A' and A_follower > B_follower:
    win = True
  elif answer == 'B' and A_follower < B_follower:
    win = True
  return win

def get_new_candidates(A, B):
  """
  This function gives the value of 'A' to 'B'
  and finds a new random element from the dictionary.
  """
  game_data.data2.append(A)
  A = B
  B = random.choice(game_data.data)
  while B in game_data.data2:
    B = random.choice(game_data.data)
    if len(game_data.data) == len(game_data.data2):
      print("Congrats You won all the game!")
      return
  return A, B

score = 0

while True:
  print(art.logo)
  if score != 0:
    print(f"You are right! Current score: {score}")
  else:
    A = random.choice(game_data.data)
    game_data.data2.append(A)
    B = random.choice(game_data.data)
    while B in game_data.data2:
      B = random.choice(game_data.data)
  print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
  print(art.vs)
  print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.")
  ans = input("Who has more followers? Type 'A' or 'B': ")
  if who_has_more_follower(A, B, ans):
    score += 1
    A, B = get_new_candidates(A, B)
  else:
    os.system("clear")
    print(art.logo)
    print(f"You lose! Current score: {score}")
    break
  os.system("clear")