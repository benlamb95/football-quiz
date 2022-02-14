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
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
    * [The Surface Plane](#The-Surface-Plane)
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

### Site Goals
* As a user I want to play a fun quiz game that is fun.
* As a user I want the questions to have ranging difficulty.
* As a user I want to be able to check my scores.
* As a user I want there to be a consistent theme and language used.

## Future Developments

One future development would be to add as many questions as possible to be able to alternate the 20 questions that could be asked to the user.
This would result in a less repetitve game meaning users wont be able to memorise the answers as easily. 

Another feature I would like to implement is to allow a player to have a second guess, however rather than get 3 points they  
would only get 1 point if the answer was correct. This would mean a more varied final table and should make it more competitive.

## Testing 
Testing was done through out the development of this quiz via the terminal in Gitpod. This project was easier to test as it runs through a terminal any way so all that was required was to test functions 
by calling them and adding print statements.  
The longest inital stage of testing was seeing whether or not the scores/points acquired by the user would add correctly to the spreadsheet. 

## Deployment

1. If not done so already `Sign up` to [Heroku](https://en.wikipedia.org/wiki/Heroku) and then `Log in`.
2. Create a `New App` from the main Heroku Dashboard.
3. Give your project a suitable name. This name must be available and unique.
4. Add `config vars` loated within the settings tab within the submenu if you have used the Code Institute Template. 
5. Add `CREDS` within the Key input field and `PORT 8000` within the Values.
6. Next add a buildpack ehich is below the above process.
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