#This function simulates a game of Rock Paper Scissors. Instead of going against another person you go against
#a computer that picks a random choice.

import random

def Rock_Paper_Scissors():
    options = ["Rock","Paper", "Scissors"]

    player_choice = input("Lets play some Rock-Paper-Scissors! Ready? Rock, Paper, Scissors, SHOOT! ")
    player_choice = player_choice.strip()
    if player_choice not in options:
        print("Sorry, that's not a valid choice. Please try again and pick Rock, Paper, or Scissors.")
        Rock_Paper_Scissors()
        return

    comp_choice = random.choice(options)
    
    if comp_choice == player_choice:
        print(f"Both you and I chose {comp_choice}. Looks like it's a tie.")
    elif player_choice == "Rock":
        if comp_choice == "Paper":
            print(f"I chose {comp_choice} and you chose {player_choice}. Looks like I win.")

        else:
            print(f"I chose {comp_choice} and you chose {player_choice}. Congratulations, you won!")
            
    elif player_choice == "Paper":
        if comp_choice == "Scissors":
            print(f"I chose {comp_choice} and you chose {player_choice}. Looks like I win.")
            
        else:
            print(f"I chose {comp_choice} and you chose {player_choice}. Congratulations, you won!")
            
    elif player_choice == "Scissors":
        if comp_choice == "Rock":
            print(f"I chose {comp_choice} and you chose {player_choice}. Looks like I win.")
            
        else:
            print(f"I chose {comp_choice} and you chose {player_choice}. Congratulations, you won!")
    
    Game2_Choice = input("Want to play again? ")
    if Game2_Choice.strip().lower()== "no":
        print("Alright. Have a good day!")
    elif Game2_Choice.strip().lower() == "yes" or "yea" or "yeah":
        print("Ok, let go!")
        Rock_Paper_Scissors()
    
Rock_Paper_Scissors()