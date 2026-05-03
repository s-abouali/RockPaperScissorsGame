# rock, paper, scissors game in python

import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
playing = True


while playing:
    player = input("Enter an option (rock, paper, scissors): ").lower()
    while player not in options:
        print("🚨🚨🚨🚨")
        player= input("Enter a valid option (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!!!!")
    elif player == "rock" and computer == "scissors":
        print("You Win!!!")
    elif player == "scissors" and computer == "paper":
        print("You Win!!!")
    elif player == "paper" and computer == "rock":
        print("You Win!!!")

    else:
        print("You Loose!!!!!")

    play_again = input("Play Again? (y/n): ").lower()
    if not play_again == "y":
        playing = False

print("Thank You For Playing!")