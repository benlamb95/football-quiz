import os
import sys
import time
from modals import Question, Team


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
    print('Welcome to my Ultimate Premier League Quiz!')
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
    time.sleep(1)
    print("\nCan you become champions?\n")
    time.sleep(1)
    print("Or will you be relagated?")
    print("-" * 25)
    time.sleep(1)
    while True:
        name = input("\nPlease enter your teams name:\n").title()
        if any(l.isdigit() for l in name):
            print("\nPlease enter letters only\n")
        else:
            print(f"Welcome {name}! Its nearly time for Kick Off!")
            break
    time.sleep(1)
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
        selected = input("\n\tType 's', 'i' or 'q':").lower().strip("")
        if selected == "s":
            start_quiz()
            break
        elif selected == "i":
            quiz_instructions()
            break
        elif selected == "q":
            quit_game()
            break
        else:
            print("\nFoul! Please choose from 's', 'i' and 'q'.")
            continue


question_prompt = [
    "Who is the all-time top goalscorer?\n \
        (a) Thierry Henry\n \
        (b) Alan Shearer\n \
        (c) Wayne Rooney\n",

    "Who tops the all-time top Assists?\n \
        (a) Ryan Giggs\n \
        (b) Cesc Fabregas\n \
        (c) Wayne Rooney\n",

    "Who holds the record for most appearances?\n \
        (a) Frank Lampard\n \
        (b) Gareth Barry\n \
        (c) Ryan Giggs\n",

    "Who has won the competition the most times?\n \
        (a) Manchester United\n \
        (b) Arsenal\n \
        (c) Chelsea\n",

    "Who holds the record for most clean sheets?\n \
        (a) David James\n \
        (b) David Seaman\n \
        (c) Petr Cech\n",

    "Who holds the record for most losses?\n \
        (a) West Ham\n \
        (b) Newcastle\n \
        (c) Everton\n",

    "When was the League founded?\n \
        (a) 1992\n \
        (b) 1991\n \
        (c) 1993\n",

    "Derby holds the record for fewest wins in a season with how many?\n \
        (a) 4\n \
        (b) 3\n \
        (c) 1\n",

    "Which club holds the record for the highest single match attendance?\n \
        (a) Tottenham\n \
        (b) Manchester United\n \
        (c) Arsenal\n",

    "What was unique about the 2020-21 season?\n \
        (a) There were more goals scored than any other season\n \
        (b) Only season in which there were more away wins than home wins\n \
        (c) No English managers in the top flight for the first time\n",

    "Which manager has taken charge of the most clubs in the Premier League ?\n \
        (a) Steve Bruce\n \
        (b) Sam Allardyce\n \
        (c) Harry Redknapp\n",

    "Who is the highest scoring African?\n \
        (a) Mohamed Salah\n \
        (b) Didier Drogba\n \
        (c) Yaya Toure\n",

    "Who is the only player to have lost two games but scored hat-tricks?\n \
        (a) Matt Le Tissier\n \
        (b) Alan Shearer\n \
        (c) Dwight Yorke\n",

    "Which club plays at the London Stadium?\n \
        (a) Chelsea\n \
        (b) Brentford\n \
        (c) West Ham\n",

    "Which club only picked four non-British players when in the Prem?\n \
        (a) Barnsley\n \
        (b) Hull City\n \
        (c) Oldham\n",

    "Which club holds the record without getting a red card?\n \
        (a) Liverpool\n \
        (b) Burnley\n \
        (c) Leicester\n",

    "Who was the top goal scorer of the first ever Premier League season?\n \
        (a) Teddy Sheringham\n \
        (b) Les Ferdinand\n \
        (c) Dean Holdsworth\n",

    "The fastest goal scored in the prem is how many seconds?\n \
        (a) 7.40 seconds\n \
        (b) 8.02 seconds\n \
        (c) 7.69 seconds\n",

    "Who has scored the most headers?\n \
        (a) Alan Shearer\n \
        (b) Peter Crouch\n \
        (c) Didier Drogba\n",

    "Wat are Leiceter City also known as?\n \
        (a) The Walkers\n \
        (b) The Kings\n \
        (c) The Foxes\n",
]


question_answer = [
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


def start_quiz():
    print("This link works")


print(welcome())
