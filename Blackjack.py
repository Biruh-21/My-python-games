import random

cards = {'A':11, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Q':10, 'J':10, 'K':10}

your_score = 0
computer_score = 0

def current_score(current_cards):
  score = 0
  for card in current_cards:
    score += cards[card]
  if score > 21 and 'A' in current_cards:
    score -= 10
  return score

def who_win(your, computer, decision):
  if your > 21 and decision == 'y':
    print(f"Your final hand: {your_cards}, final score: {your}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer}")
    print("You went over. You lose 😤")
    return False
    
  if (computer > 21 and decision == 'n') or (your > computer and decision == 'n') or your == 21:
    print(f"Your final hand: {your_cards}, final score: {your}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer}")
    print("Oponent went over. You win 😁")
    return False
  elif computer > your and decision == 'n':
    print(f"Your final hand: {your_cards}, final score: {your}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer}")
    print("You went over. You lose 😤")
    return False
wanna_play = 'y'
while wanna_play == 'y':
  hit = 'y'
  your_cards = random.sample(list(cards), 2)
  computer_cards = random.sample(list(cards), 2)
  while hit == 'y':
    your_score = current_score(your_cards)
    computer_score = current_score(computer_cards)
    print(f"Your_cards: {your_cards}, current score: {your_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    should_break = True
    should_break = who_win(your_score, computer_score, hit)
    if should_break == False:
      break
    hit = input("Type 'y' to get another cards, type 'n' to pass: ")
    new_card = random.choice(list(cards))
    your_cards.append(new_card)
  
  while computer_score < 17 and hit == 'n':
    new_card = random.choice(list(cards))
    computer_cards.append(new_card)
    computer_score = current_score(computer_cards)
  
  if hit == 'n':
    xx = who_win(your_score, computer_score, hit)
  wanna_play = input("Do you want to play again? 'y' or 'n': ") 