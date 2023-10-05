"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Miroslav Babka
email: miroslav.babka@email.cz
discord: miro3363_98687
"""
# Import libraries
from pprint import pprint
# Import own modules
from users import users
from texts import TEXTS

# Constants
SLINE = "----------------------------------------"
TERM_TEXT = "Program terminated."

# Start of the program
print("Text Analyzer")

# Request username and password
user_name = input("Username: ")
user_password = input("Password: ")
print(SLINE)
## user_name = "ann"
## user_password = "pass123"

if user_name in users and user_password == users[user_name]["password"]:
    print("Welcome to the app, ",user_name.title(),"!",sep='')
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(SLINE)
else:
    print("You are not registered user.")
    print(TERM_TEXT)
    quit()

# Select between three texts saved in TEXTS
number_of_texts = len(TEXTS)
selection_text = "Enter a number btw. 1 and " + str(number_of_texts) + " to select: "
user_choice = input(selection_text)
print(SLINE)
if not user_choice.strip().isdigit():
    print("Only numbers are accepted as a choice.")
    print(TERM_TEXT)
    quit()
else:
    sel_item = int(user_choice) - 1
    if not (sel_item >= 0 and sel_item < number_of_texts):
        print(f"Only choices between 1 and {number_of_texts} are accepted.")
        print(TERM_TEXT)
    else:
        ## Clean words from other characters and split the string to list of words
        all_words= TEXTS[sel_item].replace(".","").replace(",","").split()
        print(all_words)

        # Variables for output
        stats = {}
        max_len = 0
        titlecase_words = 0
        numeric_words = 0
        numeric_value = 0
        lowercase_words = 0
        uppercase_words = 0
        
        for word in all_words:
            # Statistics for word lengths "1","2","3"....
            if str(len(word)) in stats:
                stats[str(len(word))] += 1
            else:
                stats[str(len(word))] = 1
            # Max length of word found so far
                if len(word) > max_len:
                    max_len= len(word)
            # Count types of the words
            if word.isdigit():
                numeric_words += 1
                numeric_value += int(word)
            elif word.isalpha():
                if word.title() == word:
                    titlecase_words += 1
                    print(" - titlecase word ", word)
                if word.lower() == word:
                    lowercase_words += 1
                if word.upper() == word:
                    uppercase_words += 1

        # Format and print required output
       
        print(f"There are {len(all_words)} words in the selected text.")
        print(f"There are {titlecase_words} titlecase words.")
        print(f"There are {uppercase_words} uppercase words.")
        print(f"There are {lowercase_words} lowercase words.")
        print(f"There are {numeric_words} numeric strings.")
        print(f"The sum of all the numbers is {numeric_value}")
   
        # Header (adjusted to size of the charts)
        max_occur = int(sorted(stats.values())[-1:][0])
        space_len = max_occur - 9
        print(SLINE)
        print("LEN|  OCCURENCES"," "*space_len,"|NR.",sep='')
        print(SLINE)

        # Print all lines
        for word_len in range(1, max_len + 1):
            if str(word_len) in stats:
                space_len = max_occur - stats[str(word_len)] + 3
                print("%3d" %(word_len), '|',"*"*stats[str(word_len)]," "*space_len,'|',str(stats[str(word_len)]),sep='')
        print(SLINE)
  




        



