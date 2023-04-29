import random
print("-------Let's play Rock-Paper-Scissors-------")
player_choice = input("Enter your choice (r for rock/p for paper/s for scissors): ").lower()
computer_choice = random.choice(["r" or "R" or "rock", "p" or "P" or "paper", "s" or "S" or "scissors"])
print("Computer chooses", computer_choice)
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" or player_choice == "r" or player_choice == "R":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif player_choice == "paper" or player_choice == "p" or player_choice == "P":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif player_choice == "scissors" or player_choice == "s" or player_choice == "S":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")
