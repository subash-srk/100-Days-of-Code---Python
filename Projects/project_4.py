#R O C K , P A P E R , S C I S S O R S

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock, Paper, Scissors Game!")
import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(f"You chose {game_images[user_choice]}")

computer_choice = random.randint(0,2)
print(f"Computer chose {game_images[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
  print("You entered invalid character, you lose ")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose!")  
elif computer_choice > user_choice:
  print("You lose!")
elif user_choice > computer_choice:
  print("You win!")
else:
  print("It's a draw!")
 
  