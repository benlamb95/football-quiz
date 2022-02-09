import os
import sys
import time
import random
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from modals import Question
from questions import question_prompt

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Football Quiz')

table = SHEET.worksheet('table')

data = table.get_all_values()


def clear_console():
    """
    Clears the console function, with help
    from https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def quit_game():
    """Leaves the Quiz"""
    print("\nAn early bath for you, but try again another time!")
    time.sleep(1)
    sys.exit()


def welcome():
    """
    Print ASCII art and get users name along
    with users options
    """
    print('\nWelcome to my Ultimate Premier League Quiz!')
    print("""
                      ___
                  _.-'___'-._
                .'--.`   `.--'.
               /.'   /   \   `.
              |/    |     |    \|
              | \ .''-._.-''. / |
               \ |     |     | /
                '.'._.-'-._.'.'
                  '-:_____;-'
        \n""")
    time.sleep(2)
    print("\nCan you become champions?\n")
    time.sleep(2)
    print("Or will you be relegated?")
    print("-" * 25)
    time.sleep(2)
    print("""
            Start (s)
            Instructions (i)
            Quit (q) """)
    welcome_selection()


def quiz_instructions():
    """
    Prints the quiz instructions 
    """
    clear_console()
    print("This quiz is based on the Premier League,")
    print("The greatest league in the world!")
    print("I hope this quiz is fun yet challenging.")
    print("-" * 25)
    print()
    time.sleep(2)
    print("1. To answer a question select a, b or c.\n")
    time.sleep(2)
    print("2. The program will let you know if the answer is correct\n")
    time.sleep(2)
    print("3. You will get a point for a correct answer.\n")
    time.sleep(2)
    print(("4. Once all questions are answered, your position " 
          "will be revealed...'"))
    print()
    print("-" * 25)
    print("""
            Start (s)           
            Instructions (i)         
            Quit (q) """)
    welcome_selection()


def welcome_selection():
    """ Runs the selected option from welcome page """
    selection_options = True
    while selection_options:
        selected = input("\n\tType 's', 'i' or 'q':\n").lower().strip("")
        if selected == "s":
            clear_console()
            start_quiz(questions)
            break
        elif selected == "i":
            clear_console()
            quiz_instructions()
            break
        elif selected == "q":
            quit_game()
            break
        else:
            print("\nFoul! Please choose from 's', 'i' and 'q'.\n")
            continue


questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "b"),
    Question(question_prompt[3], "a"),
    Question(question_prompt[4], "c"),
    Question(question_prompt[5], "c"),
    Question(question_prompt[6], "a"),
    Question(question_prompt[7], "c"),
    Question(question_prompt[8], "a"),
    Question(question_prompt[9], "b"),
    Question(question_prompt[10], "b"),
    Question(question_prompt[11], "a"),
    Question(question_prompt[12], "a"),
    Question(question_prompt[13], "c"),
    Question(question_prompt[14], "c"),
    Question(question_prompt[15], "b"),
    Question(question_prompt[16], "a"),
    Question(question_prompt[17], "c"),
    Question(question_prompt[18], "b"),
    Question(question_prompt[19], "c"),

]


def start_quiz(questions):
    """
    Function to loop through questions
    randomly, and increment score & points
    """
    while True:
        name = input("\nPlease enter your teams name:\n").title()
        if any(letter.isdigit() for letter in name):
            print("\nPlease enter letters only\n")
        else:
            print(f"\nWelcome {name}! Its time for Kick Off!\n")
            break
    time.sleep(2)
    print("\n*Phwwwwwhht*\n")
    time.sleep(2.5)
    clear_console()
    score = 0
    points = 0
    random.shuffle(questions)
    for question in questions:
        while True:
            answer = input(question.prompt).lower().strip()
            if answer not in {"a", "b", "c"}:
                print("\nPlease select (a) (b) or (c) only\n")
                time.sleep(1.5)
                clear_console()
                continue
            elif answer == question.answer:
                score += 1
                points += 3
                print("\nCorrect!\n")
                time.sleep(1.5)
                clear_console()
                break
            else:
                print("\nBad luck\n")
                time.sleep(1.5)
                clear_console()
                break
    print("You got " + str(score) + " out of " +
          str(len(questions)) + " correct\n")
    print("Meaning you got " + str(points) + " points\n")
    print("Fetching your overall league position...\n")
    # Write the user to the sheet
    SHEET.worksheet("table").append_row(values=[name, score, points])
    # sort leaderboard
    table = sorted(
        SHEET.worksheet("table").get_all_values()[1:],
        key=lambda x: int(x[2]),
        reverse=True
        )
    print(tabulate(table, tablefmt='fancy_grid'))
    
    
    

def main():
    """
    Runs all main functions
    """
    welcome()


main()