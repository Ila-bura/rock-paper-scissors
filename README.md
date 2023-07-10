# Ila's Rock Paper Scissors
Ila's Rock Paper Scissors is an app that allows the users to play the old-fashioned game against the computer. 

The uninitiated user has the chance to display the rules of the game before playing the first round. 
The game consists of multiple rounds: for each round, the user is prompted to type one of the possible options then the computer will generate a random option itself. 
The possible outcomes for each round are three: the user wins, the bot wins or it is a tie. For every win, one point is assigned. Ties are not counted and the winner needs to score at least 3 points. 

Once the game is over and the results are displayed, the user is presented with the option to run the app again, or quit the application. If they decide to play again, the scores will be reset and the game will restart.

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
+ [Version Control](#version-control "Version Control")
+ [Page Deployment](#page-deployment "Page Deployment")
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
The app aims to provide light-hearted entertainment. The print statements generated are clear and to the point, prompting the user to choose their options at each turn and prevent errors by communicating clearly if the input is incorrect. 

### Current User Goals:
To keep the user entertained and engaged with the app by allowing them to play multiple games, one after the other. 

### New User Goals:
Experiment with a coomputer-based version of the old-fashioned game.

### Future Goals:
Make the game more challenging by providing more options to choose from and a leaderboard to encourage users to keep playing. Improve text readability by adding a touch of colour to the print statements.

## Design

### Wireframes:
![App functionality Wireframe](assets/images/readme-wireframe.png)

## Features

### Existing Features:

#### Landing Page:
![Landing Page](assets/images/readme-landingpage.png)
The user is greeted with a couple of fun facts regarding the original game of Rock Paper Scissors. The user is then able to choose whether to revise the rules of the game or go straight to playing.
The only viable options to choose from (Y or N) are clearly stated. If the user types any other keys or clicks enter without typing anything, an error message is displayed with the only available options. A loop makes sure that the user has the chance to type their answer again, until they type an acceptable option. 

#### Rules Refresher:
![Rules Refresher](assets/images/readme-rulesrefresher.png)
A quick summary of the main rules of the game, how points are assigned and how many are needed to win the game. In the subsequent line, the user can start playing by entering one of the possible options.

#### Possible Outcomes:
![Possible Outcomes](assets/images/readme-outcomes.png)
For each round the user and the bot's choices are displayed, as well as the partial results. If it is a tie, the user is prompted to make another choice.

#### Error Handling:
![Invalid Input](assets/images/readme-invalidinput.png)
The only viable options to choose from while playing are Rock, Paper, Scissors. The input can be typed in both uppercase and lowercase and still treated as valid.
If the user types any other keys or clicks enter without typing anything, an error message is displayed reminding them of the only three available options. A loop makes sure that the user has the chance to type their choice again, until they type an acceptable option.

#### Final Scores:
![Final Scores](assets/images/readme-finalscores.png)
As soon as either the user or the bot score 3 points, the end of the game is announced together with the final results, including the number of ties.

#### Play again or Quit app:
![Play again or Quit](assets/images/readme-quit-restart.png)
The user has the option to quit the app or keep playing. In the latter case, the game restarts and the scores are reset.

### Features Left to Implement
- Expand the app and provide more options to choose from.
- Change the colour of the print statements to improve text readability. 
- Create a leaderboard to store the best scores.

## Testing

### Validator Testing
- The code has been tested by using [CI PEP8 Online](hhttps://pep8ci.herokuapp.com/).
![PEP8 CI Validation](assets/images/readme-pep8.png)
The only error originally found was a blank line left at end of the file. This error has been fixed.

### Manual Testing
| Test            | Expected            | Outcome     |
| :-------------- | :------------------ | :---------- |
|   Open landing page             |                     | As Expected |
|                |                     | As Expected |
|                |                     | As Expected |
|                |                     | As Expected |
|                |                     | As Expected |
|                |                     | As Expected |

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