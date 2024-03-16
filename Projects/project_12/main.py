from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


print(logo)

def check_answer(guess, answer, turns):
    '''Check Answer Against Guess'''
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The number was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess,answer, turns)
        if turns == 0:
            print(f"Psst!, Correct answer is {answer}")
            print("You run out of guesses, You lose.")
            return
        elif guess != answer:
            print("Guess Again")
game()


