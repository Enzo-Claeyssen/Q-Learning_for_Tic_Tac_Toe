import random
import math
from math import exp
from .Opponent import Opponent
import csv
import numpy as np
from tqdm import tqdm




def relu(x) :
    return max(0.004 * x, x)

def relu_deriv(x) :
    if x > 0 :
        return 1
    else :
        return 0.004

class Network :
    
    def __init__(self, layers) :
        
        self.layers = layers
        self.learningRate = 0.0001
        self.alpha = 0.7
        self.nbLayers = len(layers)
        self.input = [np.matrix([0 for _ in range(layers[i + 1])]) for i in range(self.nbLayers - 1)]
        self.output = [np.matrix([0 for _ in range(layers[i])]) for i in range(self.nbLayers)]
        self.deriv = [[np.matrix([[0] for _ in range(layers[i + 1])])] for i in range(self.nbLayers - 1)]
        self.synapse = []
        self.bias = []
        self.delta = [np.matrix([[0] for _ in range(layers[i+1])]) for i in range(self.nbLayers - 1)]
        self.size = layers
        self.activation_hidden = np.vectorize(relu)
        self.derivative_hidden = np.vectorize(relu_deriv)
        self.bufferSize = 10000
        self.batchSize = 32
        self.numberOfBatch = self.bufferSize // self.batchSize
        self.buffer = []
        self.batch = []
        self.epsilon = 1
        self.decayRate = 0.00005
        self.numberOfDecay = 0
        self.epochs = 1
        
        for layerSize in layers[1:] :
            self.bias.append(np.matrix([random.random() *2 - 1 for _ in range(layerSize)]))
        
        for i in range(len(layers) - 1) :
            self.synapse.append(np.matrix([[random.random() * 2 - 1 for _ in range(layers[i+1])] for _ in range(layers[i])]))
        
    
    
    def propagate(self, state) :
        self.output[0] = np.matrix(state)
        
        for i in range(1, self.nbLayers - 1) :
            self.input[i-1] = (self.output[i-1] @ self.synapse[i-1]) + self.bias[i-1]
            self.output[i] = self.activation_hidden(self.input[i-1])
        
        self.input[-1] = (self.output[-2] @ self.synapse[-1]) + self.bias[-1]
        self.output[-1] = self.input[-1]
        return self.output[-1].tolist()[0]
    
    
    def learn_NEW(self, data) :
        self.buffer.append(data)
            
        if len(self.buffer) >= self.bufferSize :
            for _ in range(self.epochs) :
                random.shuffle(self.buffer)
                for i in range(self.numberOfBatch) :
                    self.batch = self.buffer[i*self.batchSize : (i+1) * self.batchSize]
                    self.batchLearn(self.batch)
            self.buffer = []
            self.decayEpsilon()
    
    def learn(self, data) :
        self.buffer.append(data)
            
        if len(self.buffer) >= self.bufferSize :
            for i in range(self.batchSize) :
                choice = random.randint(0, len(self.buffer)-1)
                self.batch.append(self.buffer.pop(choice))
                
            self.batchLearn(self.batch)
            self.batch = []
            self.decayEpsilon()
    
    
    def batchLearn(self, batch) :
        batchDelta = [np.matrix([[0.0] for _ in range(self.layers[i+1])]) for i in range(self.nbLayers - 1)]
        batchSynapseDelta = [np.matrix([[0.0 for _ in range(self.layers[i+1])] for _ in range(self.layers[i])]) for i in range(self.nbLayers -1)]
        
        for data in batch :
            target = self.propagate(data[0])
            action = data[1]
            reward = data[2]
            expectedCumulativeReward = target[action]
            error = reward - expectedCumulativeReward
            target[action] = expectedCumulativeReward + self.alpha * error
            
            
            for i in range(1, self.nbLayers- 1) :
                self.deriv[i-1] = self.derivative_hidden(self.input[i-1]).transpose()
            self.deriv[-1] = np.ones_like(self.input[-1]).transpose()
            
            
            self.delta[-1] = (self.output[-1] - target).transpose()
            for i in range(self.nbLayers - 3, -1, -1) :
                nextError = self.synapse[i+1] @ self.delta[i+1]
                self.delta[i] = np.multiply(self.deriv[i], nextError)

            synapseDelta = []

            for i in range(self.nbLayers - 1) :
                outRepeat = np.repeat(self.output[i].transpose(), repeats = self.delta[i].shape[1], axis = 1)
                errorRepeat = np.repeat(self.delta[i].transpose(), repeats = len(self.output[i]), axis = 0)
                synapseDelta.append(np.multiply(outRepeat, errorRepeat))
            
            
            for i in range(len(batchDelta)) :
                batchDelta[i] += self.delta[i]
            
            for i in range(len(batchSynapseDelta)) :
                batchSynapseDelta[i] += synapseDelta[i]


        for i in range(len(batchDelta)) :
            batchDelta[i] /= self.batchSize
        
        for i in range(len(batchSynapseDelta)) :
            batchSynapseDelta[i] /= self.batchSize


        for i in range(self.nbLayers - 1) :
            self.bias[i] -= self.learningRate * batchDelta[i].transpose()
            
        for i in range(self.nbLayers - 1) :
            self.synapse[i] -= self.learningRate * batchSynapseDelta[i]
    
    
    def setEpsilon(self, n) :
        self.epsilon = n + 0.05
    
    
    def decayEpsilon(self) :
        """
        Decays the epsilon, less exploration and more exploitation
        """
        self.epsilon = 0.05 + 0.95 * exp(-1 * self.decayRate * self.numberOfDecay)
        self.numberOfDecay += 1








class DQN(Opponent) :
    
    
    __ANN = Network([9, 200, 200, 9])
    
    
    def __init__(self, symbole, trainingMode) :
        """
        Initialize hyperparameters
        :param: symbole The symbole used by this opponent
        :param: trainingMode True if in trainingMode False otherwise.
        """
        super().__init__(symbole)
        self.trainingMode = trainingMode
        self.__learningRate = 0.7
    
    
    def makeAction(self, state) :
        """
        Returns the action made by the opponent
        :param: state The state where the action is taken.
        :return: An int representing the action
        """
        processed = self._linearState(state)
        if self.trainingMode :
            action = self.__epsilonGreedyPolicy(processed)
        else :
            action = self.__greedyPolicy(processed)
        return action
    
    
    def learn(self, state, action, reward) :
        """
        Updates the QTable using TDLearning
        :param: state The initial state as a grid of Cell where the action has been taken
        :param: action The action that has been made
        :param: reward The immediate reward obtained
        :param: newState The state as a grid of Cell of the env once the other opponent played
        """
        DQN.__ANN.learn((self._linearState(state), action, reward))
        
        
    @staticmethod
    def importData() :
        filename = 'weight-layer'
        for i in range(len(DQN.__ANN.synapse)) :
            #Does NOT need to be closed since it is npy file
            DQN.__ANN.synapse[i] = np.load('models/DQN/' + filename + str(i) + '.npy', allow_pickle = False)
        
        filename = 'bias-layer'
        for i in range(len(DQN.__ANN.bias)) :
            DQN.__ANN.bias[i] = np.load('models/DQN/' + filename + str(i) + '.npy', allow_pickle = False)
            
        
    
    @staticmethod
    def exportData() :
        filename = 'weight-layer'
        for i in range(len(DQN.__ANN.synapse)) :
            np.save('models/DQN/'+ filename + str(i), DQN.__ANN.synapse[i], allow_pickle=False) # Keep allow_pickle=False for security !!!!
        
        filename = 'bias-layer'
        for i in range(len(DQN.__ANN.bias)) :
            np.save('models/DQN/' + filename + str(i), DQN.__ANN.bias[i], allow_pickle=False)
    
    @staticmethod
    def importData_OLD() :
        """
        Imports the QTable
        """
        with open('models/DQN.csv', 'r') as file :
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            
            size = len(DQN.__ANN.layers)
            for i in range(size) :
                layerSize = len(DQN.__ANN.layers[i])
                bias = list(next(reader))
                for j in range(layerSize) :
                    DQN.__ANN.layers[i][j].biais = bias[j]
            
            size = len(DQN.__ANN.synapse)
            for i in range(size) :
                layerSize = len(DQN.__ANN.synapse[i])
                for j in range(layerSize) :
                    nbSynapse = len(DQN.__ANN.synapse[i][j])
                    weights = list(next(reader))
                    for k in range(nbSynapse) :
                        DQN.__ANN.synapse[i][j][k].weight = weights[k]
                
    
    
    @staticmethod
    def exportData_OLD() :
        """
        Exports the QTable
        """
        size = len(DQN.__ANN.layers)
        bias = [[] for _ in range(size)]
        for i in range(size) :
            layerSize = len(DQN.__ANN.layers[i])
            for j in range(layerSize) :
                bias[i].append(DQN.__ANN.layers[i][j].biais)
        
        size = len(DQN.__ANN.synapse)
        weights = [[] for _ in range(size)]
        for i in range(size) :
            layerSize = len(DQN.__ANN.synapse[i])
            weights[i] = [[] for _ in range(layerSize)]
            for j in range(layerSize) :
                nbSynapse = len(DQN.__ANN.synapse[i][j])
                for k in range(nbSynapse) :
                    weights[i][j].append(DQN.__ANN.synapse[i][j][k].weight)
        
        with open('models/DQN.csv', 'w') as file :
            writer = csv.writer(file)
            writer.writerows(bias)
            
            for data in weights :
                writer.writerows(data)
                    
            
            
        
    
    @staticmethod
    def resetQTable() :
        """
        Resets the QTable
        """
        pass


    def __greedyPolicy(self, state) :
        """
        Takes an action according to the greedyPolicy.
        :param: state The state as an int where the action has to be taken
        :return: An int describing the action maximizing expected cumulative reward
        """
        possibilities = DQN.__ANN.propagate(state)
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
        if random.uniform(0, 1) <= DQN.__ANN.epsilon :
            return random.randint(0, 8)
        else :
            return self.__greedyPolicy(state)
        

