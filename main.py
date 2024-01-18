# Import the random module
import random

# Define a function to roll a dice
def roll_dice():
  # Return a random integer between 1 and 6
  return random.randint(1, 6)

# Define a function to play the game
def play_game():
  # Initialize the scores of the player and the computer
  player_score = 0
  computer_score = 0

  # Loop until one of the scores reaches 10 or more
  while player_score < 10 and computer_score < 10:
    # Ask the player if they want to roll the dice
    answer = input("Do you want to roll the dice? (y/n) ")

    # If the answer is yes, roll the dice for the player and the computer
    if answer == "y":
      # Roll the dice for the player
      player_roll = roll_dice()
      # Print the result
      print(f"You rolled a {player_roll}")
      # Add the result to the player's score
      player_score += player_roll

      # Roll the dice for the computer
      computer_roll = roll_dice()
      # Print the result
      print(f"The computer rolled a {computer_roll}")
      # Add the result to the computer's score
      computer_score += computer_roll

      # Print the current scores
      print(f"Your score: {player_score}")
      print(f"Computer's score: {computer_score}")

    # If the answer is no, end the game
    elif answer == "n":
      print("You quit the game.")
      break

    # If the answer is invalid, ask again
    else:
      print("Invalid input. Please enter y or n.")

  # Check who won the game
  if player_score >= 10:
    print("You win!")
  elif computer_score >= 10:
    print("The computer wins!")
  else:
    print("No one wins.")

play_game()
