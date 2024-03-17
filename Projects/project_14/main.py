from art import logo,vs
# from replit import clear
from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(user_ch,a_followers, b_followers):
    if a_followers > b_followers:
        return user_ch == 'a'
    else:
        return user_ch == 'b'



print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    user_ch = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = check_answer(user_ch , a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f"You're Right!, Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, You're Wrong. Final Score: {score}")







