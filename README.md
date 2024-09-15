# DeepRLTesting
Using RL and DeepRL algorithms to create models able to play TicTacToe


## How to use ?

- Download the zip of the lastest release
- Unzip
- Open shell within "DeepRLTesting" folder
- Type make

#### First time use ?
Generates doc + runs the program and install depedencies.
- make

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



## State of project : Q-Learning agent works, DQN W.I.P
- Features tic tac toe game
- Random Opponent (playing totally randomly)
- Q-Learning Agent using tabular Q-learning
- DQN Agent using neural network (W.I.P)
- Pre-Trained models ready to be imported (see Import/Export within the program)
- Able to export your own model to re-import it later


## Scheduled : DQN

### Already Done
- DENSE network generation
- Feed Forward + Backpropagation with numpy
- Mini-Batch Learning
- First Pre-Trained DQN Agent


### TODO
- Generate a perfect pre-trained DQN agent (perfect agent = solved tic tac toe)
- Make sure a perfect agent is generated each time training is done from scratch

