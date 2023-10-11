"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Miroslav Babka
email: miroslav.babka@email.cz
discord: miro3363_98687
"""
import random
from time import time
# from time import strftime
# from time import gmtime

# Strings
msg_welcome = """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:"""
msg_input = ">>> "
msg_separator = "-----------------------------------------------"
msg_bad_input = "Enter 4 unique digits please"
msg_final_result = """Correct, you've guessed the right number 
in {} guesses!"""
msg_bulls = {True : "bull", False : "bulls"}
msg_cows = {True : "cow", False : "cows"}
msg_evaluation_grades = {0 : "amazing", 1 : "average", 2: "not so good"}
msg_evaluation = "That's {}"
msg_time_elapsed = "Elapsed time {} seconds"
msg_next_game = "Another game Y/N? "
msg_game_score = "Score: "
msg_game_score_row = " {}. {} guesses in {} seconds"

# Set game related values
game_results = {}
game_count = 0
next_play = 'y'

# Code
print("Bulls & Cows \n")
# Multiple games enabled
while next_play == "y":
    # Set basic control values
    not_quessed = True
    guess_count = 0
    secret_list = [0, 0, 0, 0]
    # Generate the secret number (four unique digits)
    while secret_list[0] == 0:
        secret_list = random.sample([0,1,2,3,4,5,6,7,8,9], 4)
    # print(secret_list)
    print(" ")

    print(msg_welcome)
    start_time = time()

    # Game loop
    while not_quessed :
        bulls = 0
        cows = 0
        print(msg_separator)
        new_guess = input(msg_input).strip()
        # Test input leading zero, correct length and digits only
        if (new_guess[0] == '0') or (len(new_guess) != 4) or (not new_guess.isdigit()):
            print(msg_bad_input)
            continue
        # Test input for unique digits
        elif list(new_guess) != list({x:x for x in new_guess}.values()):
            # if list(new_guess) != list(dict.fromkeys(new_guess)):
            print(msg_bad_input)
            continue
        # Correct input
        else:
            guess_count += 1
            # Count cows and bulls
            guess_list = [int(x) for x in new_guess]
            for x in range(4):
                if guess_list[x] == secret_list[x]:
                    bulls += 1
                elif guess_list[x] in secret_list:
                    cows += 1
            # Print result                
            print(f"{bulls} {msg_bulls[bulls < 2]}, {cows} {msg_cows[cows < 2]}")
            if bulls == 4:
                not_quessed = False
                # Print number of guesses used
                print(msg_final_result.format(guess_count))
                print(msg_separator)
                # Print evaluation 1 - 4 amazing, 5 - 9 average, > 10 not so good
                final_result = guess_count // 5
                if final_result > 2:
                    final_result = 2
                print(msg_evaluation.format(msg_evaluation_grades[final_result]))
                # Print elapsed time
                elapsed_time = int(time() - start_time)
                print(msg_time_elapsed.format(elapsed_time))           
                print(msg_separator)
                
                # Save game result and print statistics
                game_results[game_count] = [guess_count, elapsed_time]
                game_count += 1
                print(msg_game_score)
                for x in range(0, len(game_results)):
                    print(msg_game_score_row.format(x+1, game_results[x][0], game_results[x][1]))
                print(msg_separator)

    # Another game?                
    next_play = input(msg_next_game).lower()