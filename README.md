# Ila's Rock Paper Scissors
Ila's Rock Paper Scissors is an app that allows the users to play the old-fashioned game against the computer. For the uninitiated, the users has the chance to display the rules of the game. The game consists of multiple rounds: for each round, the user is prompted to type one of the possible options then the computer will generate a random option itself. The possible outcomes of each round are three: the user wins, the bot wins or it is a tie. For every win, one point is assigned. Ties are not counted and the winner needs to score at least 3 points. Once the game is over and the results are displayed, the user is presented with the option to run the app again, or quit the application. If they decide to play again, the scores will be reset and the game will restart.

![Site view across devices](assets/images/readme-amiresponsive.png)

Ila's Rock Paper Scissors site is live, the link can be found [HERE](https://rock-paper-scissors-by-ila-72f68cf0d429.herokuapp.com/)

## Table of Contents
+ [UX](#ux "UX")
  + [Site Purpose](#site-purpose "Site Purpose")
  + [Site Goal](#site-goal "Site Goal")
  + [Audience](#audience "Audience")
  + [Communication](#communication "Communication")
  + [Current User Goals](#current-user-goals "Current User Goals")
  + [New User Goals](#new-user-goals "New User Goals")
+ [Design](#design "Design")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## UX

### Site Purpose:
To allow users to challenge the computer playing the Rock Paper Scissors game.

### Site Goal: 
To provide a simple and fun platform to try their luck and have fun in anticipating the computer's random choice.

### Audience:
Anyone passionate about computer games based on luck.

### Communication:
Despite its simplicity, the app aims to provide lighthearted entertainment. The print statements generated are clear and to the point, prompting the user to choose their options at each turn and prevent errors by communicating clearly if the input is incorrect. 

### Current User Goals:
To keep the user entertained and engaged with the app by allowing them to play multiple games, one after the other. 

### New User Goals:
Experiment with the coomputer-based version of an old-fashioned game.

### Future Goals:
Make the game more challenging by providing more options to choose from and a leaderboard to encourage users to keep playing. Improve text readability by adding a touch of colour to the print statements.

## Design

### Wireframes:
![App functionality Wireframe](assets/images/readme-wireframe.png)

## Features

### Existing Features:

#### Landing Page:
![Landing Page](assets/images/readme-landingpage.png)

####

####

#### Play again or Quit app:
![Play again or Quit](assets/images/readme-quit-restart.png)

### Features Left to Implement
- Expand the app and provide more options to choose from.
- Change the colour of the print statements to improve text readability. 
- Create a leaderboard to store the best scores.

## Testing

### Validator Testing
- The code has been tested by using [PEP8 Online](http://pep8online.com/).
![PEP8 Validation](assets/images/readme-pep8.png)
The only error found was a blank line left at end of the file. This error has been fixed.

### Unfixed Bugs
None that I am aware of as of now.

## Technologies Used
### Main Languages Used
- Python

### Frameworks, Libraries & Programs Used
- GitHub - to store the repository for submission.
- Lucid - to create the mock up in preparation for the project.
- Heroku - to deploy the live version of the terminal

## Deployment
The site was deployed to Heroku. The steps to deploy are as follows:
- log in to heroku
- create a new app
- navigate to settings
- add the following KEY/VALUE pair:
- - PORT + 8000
- add build packs (in this order)
- - Python
- - nodejs
- go to GitPod terminal
- type the following commands into the terminal:
- - heroku login -i
- - enter in username + password
- - heroku apps
- - heroku git:remote -a my-app-name 
- - git add .
- - git commit -m "Deploy to Heroku cia CLI"
- - git push origin main
- - git push heroku main
- The live link can be found [HERE - Ila's Rock Paper Scissors](hhttps://rock-paper-scissors-by-ila-72f68cf0d429.herokuapp.com/)
- * Site has been deployed to [Heroku](https://heroku.com/), following these [instructions]().

## Credits

### Content