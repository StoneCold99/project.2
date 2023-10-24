import random


moves = ["rock", "paper", "scissors"]

while True:

  user_move = input("What is your move? (rock, paper, scissors): ")

  computer_move = random.choice(moves)

  print("You chose:", user_move)
  print("Cortana chose:", computer_move)

  if user_move == computer_move:
    print("It's a tie!")
  elif user_move == "rock" and computer_move == "scissors":
    print("You win!")
  elif user_move == "paper" and computer_move == "rock":
    print("You win!")
  elif user_move == "scissors" and computer_move == "paper":
    print("You win!")
  else:
    print("Computer wins!")

  play_again = input("Do you want to play again? (y/n): ")
  if play_again == "n":
    break
