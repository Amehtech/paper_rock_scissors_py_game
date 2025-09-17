#ABOUT THE GAME
'''the rock-paper=scissors (RPS) is a popular hand game played between two people.
how it works
players usually counts one to three then simultaneously throw of the three hand signal
1. rock: a close fist
2. paper: a flat hand wiith fingers together
3. scissors: a v-shape made with the index and mid-fingers
# wiinning combinations:
1 rock beats scissors(rock crushes scissors)
2. scissors beats paper(scissors cuts paper)
paper beats rock (paper covers rock)'''
# IMPORT FUNCTIONALITIES
import random


game_list = ['rock','paper','scissors'] #this container stores the paper-rock-scissors
comp_choice = random.choice(game_list)

# sketch of  a rock
rock =     ( '\n        ==========\n'
          '     =================\n'
        '   =====================\n'
        '   =====================\n'
         '     ===================\n'
            '       =============\n' )

#sketch of a scissors
scissors = ('\n     ((|||||||||\\\\\\\//=============================\n    (((|||    |||\\\\\////============================\n  ((((||       |||\\\////\n  ((((||      ||||||\\\\\\\\\n    ((((|||     ||||///\\\\\============================\n     ((||||||||||//////\\\\\==========================')

# sketch of paper
paper = ('\n ===========================\n ===========================\n ===========================\n ===========================\n ===========================\n ===========================\n ===========================\n ===========================\n ===========================\n')



print("============================================================================================================================================================================================")
print("============================================================================================================================================================================================")
print("======================================================================WELCOME TO HOMEBOY-TECH SOFTWARE SOLUTION=============================================================================")
print("================================================================YOU ARE ABOUT TO BEGIN THE PAPER-ROCK-SCISSORS GAME==========================================================================")
print("============================================================================================================================================================================================")
print("============================================================================================================================================================================================")



# definition of activity for the program. this tells how the program should go about
def main_game():
    user_guess = input("---------------------------------------------------------Enter your guess: (paper, scissor or rock)!:---------------------------------------\n ").lower()
    if user_guess not in ['rock','paper','scissors']:
        print(
            "---------------------------------------------------------------------you have typed a wrong option check and try again--------------------------------------------")
        print(main_game())

    if user_guess == comp_choice:
        try_again = input(f"-------------------YOU CHOSE '\n {user_guess.upper()}' \nAND COMPUTER CHOSE '{comp_choice.upper()}'IT'S A DRAW! WOULD YOU LOVE TO TRY AGAIN? 'YES' OR 'NO'--------------------------------------------\n").lower()
        if try_again =='yes':
            return main_game()
        return None

    #
    elif  user_guess == 'rock' and comp_choice == 'paper':
            print(f"----------------------------------------YOU LOSE! YOU CHOSE '{user_guess.upper()}' AND COMPUTER CHOSE '{comp_choice.upper()}'-----------------------------")
            print(f"YOU CHOSE \n{rock}  AND THE COMPUTER CHOSE   \n{paper}")
            try_again = input(f"-------------------YOU LOSE!'\n{user_guess.upper()}' WAS COVERED BY '\n{comp_choice.upper()}' WOULD YOU LOVE TO TRY AGAIN? 'YES' OR 'NO'--------------------------------------------\n").lower()
            if try_again == 'yes':
                return main_game()
            else:
                print("---------------------------------------------------------------------------==============GAME OVER===============---------------------------------------------")
                return None
    #
    elif  user_guess == 'rock' and comp_choice == 'scissors':
            print(f"----------------------------------------YOU LOSE! YOU CHOSE '{user_guess.upper()}' AND COMPUTER CHOSE '{comp_choice.upper()}'-----------------------------")
            print(f"YOU CHOSE! + str\n{rock}   \nAND THE COMPUTER CHOSE  + \n{scissors}")
            try_again = input(f"------------------------------YOU wIN! '\n{user_guess.upper()} CRUSHED {comp_choice.upper()} WOULD YOU LOVE TO TRY AGAIN? 'YES' OR 'NO'--------------------------------------------\n").lower()
            if try_again == 'yes':
                return main_game()
            else:
                print("---------------------------------------------------------------------------------==============GAME OVER===============--------------------------------------------------------")
                return None

    #
    elif  user_guess == 'paper' and comp_choice == 'rock':
            print(f"----------------------------------------YOU WIN! YOU CHOSE '{user_guess.upper()}' AND COMPUTER CHOSE '{comp_choice.upper()}'-----------------------------")
            print(f"YOU CHOSE! \n{paper} \nAND THE COMPUTER CHOSE   \n{rock}")
            try_again = input(f"-------------------YOU wIN! '{user_guess.upper()}' COVERS '{comp_choice.upper()}' WOULD YOU LOVE TO TRY AGAIN? 'YES' OR 'NO'--------------------------------------------\n").lower()
            if try_again == 'yes':
                return main_game()
            else:
                print("------------------------------==============GAME OVER===============--------------------------------")
                return None

    #
    elif  user_guess == 'paper' and comp_choice == 'scissors':
            print(f"----------------------------------------YOU LOSE! YOU CHOSE '{user_guess.upper()}' AND COMPUTER CHOSE '{comp_choice.upper()}'-----------------------------")
            print(f"YOU CHOSE! + \n{paper} AND THE COMPUTER CHOSE  \n {scissors}")
            try_again = input(f"-------------------YOU LOSE! '{user_guess.upper()}' WAS SLICED BY '{comp_choice.upper()}' WOULD YOU LOVE TO TRY AGAIN? 'YES' OR 'NO'--------------------------------------------\n").lower()
            if try_again == 'yes':
                return main_game()
            else:
                print("------------------------------==============GAME OVER===============--------------------------------")
                return None

    #
    elif  user_guess == 'scissors' and comp_choice == 'rock':
            print(f"----------------------------------------YOU LOSE! YOU CHOSE '{user_guess.upper()}' AND COMPUTER CHOSE '{comp_choice.upper()}'-----------------------------")
            print(f"YOU CHOSE! \n{scissors} \nAND THE COMPUTER CHOSE  \n {rock}")
            try_again = input(f"-------------------YOU LOSE! '{user_guess.upper()}' WAS CRUSHED BY '{comp_choice.upper()}' WOULD YOU LOVE TO TRY AGAIN? 'YES' OR 'NO'--------------------------------------------\n").lower()
            if try_again == 'yes':
                return main_game()
            else:
                print("------------------------------==============GAME OVER===============--------------------------------")
                return None

    #
    elif  user_guess == 'scissors' and comp_choice == 'paper':
            print(f"----------------------------------------YOU WIN! YOU CHOSE '{user_guess.upper()}' AND COMPUTER CHOSE '{comp_choice.upper()}'-----------------------------")
            print(f"YOU CHOSE! \n{scissors} \nAND THE COMPUTER CHOSE  \n{paper}")
            try_again = input(f"-------------------YOU WIN! '{user_guess.upper()}' SLICED '{comp_choice.upper()}' WOULD YOU LOVE TO TRY AGAIN? 'YES' OR 'NO'--------------------------------------------\n").lower()
            if try_again == 'yes':
                return main_game()
            else:
                print("---------------------------------------------------------------==============GAME OVER===============-------------------------------------------------------------------------")
                return None
    return None


# This function call the entire program

main_game()

#end of program# paper_rock_scissors_py_game
this a python code for the paper, scissors and rock game
