from .Opponent import Opponent
from math import exp
import random
import csv


class QLearningTTT(Opponent) :
    """
    QLearning to play tic tac toe
    """
    
    __QTable = [[0 for _ in range(9)] for _ in range(19683)]
    
    
    def __init__(self, symbole, trainingMode) :
        """
        Initialize hyperparameters
        :param: symbole The symbole used by this opponent
        :param: trainingMode True if in trainingMode False otherwise.
        """
        super().__init__(symbole)
        self.trainingMode = trainingMode
        self.__epsilon = 1
        self.__decayRate = 0.0005
        self.__numberOfDecay = 0
        self.__discountFactor = 0.99
        self.__learningRate = 0.7
    
    
    def makeAction(self, state) :
        """
        Returns the action made by the opponent
        :param: state The state where the action is taken.
        :return: An int representing the action
        """
        processed = self._processState(state)
        if self.trainingMode :
            action = self.__epsilonGreedyPolicy(processed)
        else :
            action = self.__greedyPolicy(processed)
        return action
    
    
    def learn(self, state, action, reward, newState) :
        """
        Updates the QTable using TDLearning
        :param: state The initial state as a grid of Cell where the action has been taken
        :param: action The action that has been made
        :param: reward The immediate reward obtained
        :param: newState The state as a grid of Cell of the env once the other opponent played
        """
        initialState = self._processState(state)
        finalState = self._processState(newState)
        
        nextAction = self.__greedyPolicy(finalState)
        calculatedCumulativeReward = reward + self.__discountFactor * QLearningTTT.__QTable[finalState][nextAction]
        
        expectedCumulativeReward = QLearningTTT.__QTable[initialState][action]
        error = calculatedCumulativeReward - expectedCumulativeReward
        
        QLearningTTT.__QTable[initialState][action] = expectedCumulativeReward + self.__learningRate * (error)
    
    @staticmethod
    def importQTable() :
        """
        Imports the QTable
        """
        newQTable = []
        with open('models/QTableTTT.csv', 'r') as file :
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            newQTable = list(reader)
        QLearningTTT.__QTable = newQTable
    
    @staticmethod
    def exportQTable() :
        """
        Exports the QTable
        """
        with open('models/QTableTTT.csv', 'w') as file :
            writer = csv.writer(file)
            writer.writerows(QLearningTTT.__QTable)
    
    @staticmethod
    def resetQTable() :
        """
        Resets the QTable
        """
        QLearningTTT.__QTable = [[0 for _ in range(9)] for _ in range(19683)]
    
    
    def decayEpsilon(self) :
        """
        Decays the epsilon, less exploration and more exploitation
        """
        self.__epsilon = 0.05 + 0.95 * exp(-1 * self.__decayRate * self.__numberOfDecay)
        self.__numberOfDecay += 1
    
    
    def __greedyPolicy(self, state) :
        """
        Takes an action according to the greedyPolicy.
        :param: state The state as an int where the action has to be taken
        :return: An int describing the action maximizing expected cumulative reward
        """
        possibilities = QLearningTTT.__QTable[state]
        maxi = possibilities[0]
        maxi_i = 0
        for i in range(1, 9) :
            tmp = possibilities[i]
            if tmp > maxi :
                maxi = tmp
                maxi_i = i
        return maxi_i
    
    
    def __epsilonGreedyPolicy(self, state) :
        """
        Takes an action according to the epsilon greedy policy.
        With a probability of epsilon, will take a random action.
        With a probability of 1-epsilon, will act the same way as the greedy policy
        :param: state The state as an int where the action has to be taken.
        :return: An int describing the action
        """
        if random.uniform(0, 1) <= self.__epsilon :
            return random.randint(0, 8)
        else :
            return self.__greedyPolicy(state)