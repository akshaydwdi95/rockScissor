import random

# Define the rules of the game
rules = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def get_user_choice():
    choices = list(rules.keys())
    print("Choose one of the following: ", ", ".join(choices))
    user_choice = input().lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose again.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(list(rules.keys()))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in rules[user_choice]:
        return f"You win! {user_choice.capitalize()} beats {computer_choice}."
    else:
        return f"You lose! {computer_choice.capitalize()} beats {user_choice}."

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
