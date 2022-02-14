# Welcome to my Football quiz in Python!

## Introduction
---

Football is one of my true passions in life and attending quiz nights is another; so what better to combine them both and create a python game which will help with my personal development using the python language?! \
And count towards my third Project Milestone with Code Institute.

The [Premier League](https://www.premierleague.com/) is the most watched league in the world as it is the most challenging and competitive. So with this quiz I to hope it will be challenging but fun!


## Table of Contents

* [User Experience](#UX)
    * [Site Goals](#Site-Goals)
    * [User Stories](#User-Stories)
    * [Flow Diagrams](#Flow-Diagram)
    * [The Data Model](#The-Data-Model)
* [Features](#features)
* [Future Developments](#future-developments)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
----
## UX
### Site Goals
* To provide a fun quiz game that resides within a python Terminal
* To provide users an easy to use and follow page structure with simple commands
* To provide users feedback for both correct and incorrect answers as well as incorrect commands; producing error messages.

### User Stories
* As a user I want to play a fun quiz game that is fun.
* As a user I want the questions to have ranging difficulty.
* As a user I want to be able to check my scores.
* As a user I want there to be a consistent theme and language used.

## Flow Diagrams
To help me understand what I wanted to do within this project I intially drew my logic on a piece of paper. I was then recommended to use Lucid Chart by my mentor to present this electronically. By drawing out the flow of my game it massively helped me to understand the steps needed. Below I have included my flow Diagrams.

Start of game:
![Screenshot of the Start of game flow diagram](/documentation/starting-logic.png "Screenshot of the Start of game flow diagram")

Game Logic:
![Screenshot of the game flow diagram](/documentation/game-logic.png "Screenshot of the game flow diagram")

## The Data Model
I decided to use the Questions class to hold all the quiz questions and answers. Whilst building my game I also tried to introduce a player class but had left this a little bit too late as I had already built a structure for my game to follow. 

## Features

#### Welcome page
* Basic and to the point introduction
* ASCII art of a football to enhance the design and make it feel arcadey.
* 3 clear well defined instruction options
* User input validation- If user selects anything other than 's', 'i' or 'q' an error message appears.
![Screenshot of the welcome page](/documentation/welcome-screen.png "Screenshot of the welcome page")

#### Instructions page
* Bullet pointed list that is presented one at a time with a small delay for readability and interactive feel.
* Easy to follow Instructions with user input validation
![Screenshot of the Instructions page](/documentation/instructions-page.png "Screenshot of the Instructions page")

#### Name input
* Allows users to create a team name
* The name must be letters only- with feedback for any name with any numbers in
* The game will then welcome them with their name Titled and any unwanted spaces removed
![Screenshot of Name inout page](/documentation/name-page.png "Screenshot of Name Page")

#### Questions
* Questions are delivered one at a time-clearing the console each time for readability
![Screenshot of Questions](/documentation/questions-page.png "Screenshot of Questions")
* User input feedback again if any letter other than 'a', 'b' or 'c' entered and the console cleared with just the question again.
* Users are also notified whether or not the question was answered correctly or not.
![Screenshot of Questions input](/documentation/input-validation.png "Screenshot of Questions input")

#### Result
* Once all questions are answered the user is presented with a breakdown of their total score, points and that the table is being created.
![Screenshot of result](/documentation/result.png "Screenshot of result")

#### Table
* The results of the user is also presented within a table. I wanted to include current Premier League teams as a start off to make users feel they are top of the league. (Man Utd being top is probably bias ;) )  
![Screenshot of Table](/documentation/table.png "Screenshot of Table")

#### Final message 
* There are 4 final messages based on the total points gained by the user.  
![Screenshot of Final Message](/documentation/final-message.png "Screenshot of Final message")

## Future Developments

One future development would be to add as many questions as possible to be able to alternate the 20 questions that could be asked to the user.
This would result in a less repetitve game meaning users wont be able to memorise the answers as easily. 

Another feature I would like to implement is to allow a player to have a second guess, however rather than get 3 points they  
would only get 1 point if the answer was correct. This would mean a more varied final table and should make it more competitive.

## Testing 
Testing was done through out the development of this quiz via the terminal in Gitpod. This project was easier to test as it runs through a terminal any way so all that was required was to test functions 
by calling them and adding print statements.  
The longest inital stage of testing was seeing whether or not the scores/points acquired by the user would add correctly to the spreadsheet.   
![Screenshot of Final Table](/documentation/terminal-testing.png "Screenshot of Final table")  
Testing was also conducted within the Code Institute Heroku terminal.

### Validator Testing
I have tested my project within the [pep8online.com](http://pep8online.com/). The below screenshots prove this:  
#### Main Game
![Screenshot of the pep8online validator tool results](/documentation/pep8-testing.png "Screenshot of the pep8online validator tool for main game")
#### Questions
![Screenshot of the pep8online validator tool results](/documentation/pep8-questions.png "Screenshot of the pep8online validator tool for questions")
#### Modals
![Screenshot of the pep8online validator tool results](/documentation/pep8-modals.png "Screenshot of the pep8online validator tool for modals")

## Bugs
The only bug that I still have is when the user submits their result to my linked spreadsheet, it doesnt go in value order like it does within the terminal; however this shouldn't impact the user in anyway.

## Deployment

1. If not done so already `Sign up` to [Heroku](https://en.wikipedia.org/wiki/Heroku) and then `Log in`.
2. Create a `New App` from the main Heroku Dashboard.
3. Give your project a suitable name. This name must be available and unique.
4. Add `config vars` loated within the settings tab within the submenu if you have used the Code Institute Template. 
5. Add `CREDS` within the Key input field and `PORT 8000` within the Values.
6. Next add a buildpack which is below the above process.
7. Ensure `Python` is the first build pack and `Node.js` is second. You can drag and drop them to ensure this.
8. Next connect your GitHub account and follow all steps prompted. Locate the repositary by searching for its name.
9. You can then choose whether you wish to enable automatic deployments or manual. Initially I chose manual so I am in control of any changes.

## Credits
* I used Mike Dane (https://www.youtube.com/watch?v=SgQhwtIoQ7o&list=PLLAZ4kZ9dFpMMs5lskzBApYXn0bl7emsW&index=32) youtube tutorial to help structure my quiz section.
* Inspiration to linking the Google Sheets to my python file from the Love Sandwiches run through project with Code Institute.
* Tutor within Code institute for their invaluable feedback and help. Sean Tutor helped with the table creation.
* Slack to ask questions and look at previous answers. 
* (https://www.delftstack.com/howto/python/python-clear-console/) How to clear a console
* (https://www.asciiart.eu/sports-and-outdoors/soccer) for the initial ball image

### Content
The content was sourced direct from [Premier League](https://www.premierleague.com/) website. I created some questions myself and used (https://quiz-questions.uk/premier-league-football-quiz/) \
 as well as (https://www.theguardian.com/football/2021/dec/09/football-quiz-premier-league-nuggets)