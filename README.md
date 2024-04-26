# DeepRLTesting
Using DeepRL to create an AI able to play generalized versions of Power4 and TicTacToe


## How to use ?


#### First time use ?
Generates doc + runs the program.
- Use make command

#### Creating docs
Generates doc of the project.
- make doc

#### Consulting docs

- Go to doc directory and open src.html


#### Running tests
Makes sure the code is correct
- make test


#### Running Program
Use this to run the program without generating doc again.
- make run



## State of project : v0.1


Interactive version of Tic Tac Toe Game


- UML : v0.2
- Doc + Test : v0.2
- Code : v0.1


## Scheduled Versions

### Already Done

#### Creation of basic environment

- v0.0.1
Creating RandomPlayer and Opponent

- v0.0.2
Creating Cell and Board

- v0.0.3
Creating everything in Game but play()

- v0.0.4
Game.play() only with randomPlayers

- v0.0.5
Creating Player

- v0.0.6
Main Menu to choose players.

- v0.0.7
Create next version of Game.play()

- v0.0.8
Create Game.getState() and Game.step(action)

- v0.0.9
Update Opponent.makeDecision(state) and create Opponent.learn(initialState, action, reward, finalState)


#### Creation of first AI

- v0.1
Create QLearning for tic tac toe class and helper methods :
constructor + attributes + setEpsilon + updateEpsilon + policies + resetQTable


### Next versions

- v0.2
makeAction and learn for QLearningTTT

- v0.3
Include QLearning to Main Menu (with training mode)

- v0.4
Import/Export QTable from/to a file

- v1
AI works for Tic Tac Toe

- v2
AI works for Tic Tac Toe + Power 4

- v3
AI works for generalized game
