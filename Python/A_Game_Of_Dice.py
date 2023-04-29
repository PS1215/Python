import random
print("-----Let's play a game of dice-----")
player1_name = input("Enter player 1 name: ")
player2_name = input("Enter player 2 name: ")
while True:
    input(f"\n{player1_name}, press enter to roll the dice.")
    player1_roll = random.randint(1, 6)
    print(f"{player1_name} rolled {player1_roll}!")
    
    input(f"\n{player2_name}, press enter to roll the dice.")
    player2_roll = random.randint(1, 6)
    print(f"{player2_name} rolled {player2_roll}!")
    
    if player1_roll > player2_roll:
        print(f"{player1_name} wins!")
    elif player1_roll < player2_roll:
        print(f"{player2_name} wins!")
    else:
        print("It's a tie!")
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
