import random
import math
from math import exp
from .Opponent import Opponent
import csv


class Neuron :
    
    def __init__(self) :
        self.value = 0
        self.biais = random.random() * 2 - 1
        self.prev_synapse = []
        self.next_synapse = []
        self.error = 0
        self.isOutput = False
    
    def setPrevSynapse(self, prev_synapse) :
        self.prev_synapse = prev_synapse
    
    def setNextSynapse(self, next_synapse) :
        self.next_synapse = next_synapse
    
    def setBiais(self, biais) :
        self.biais = biais
    
    def getBiais(self) :
        return self.biais
    
    def setValue(self, value) :
        self.value = value
    
    def getValue(self) :
        return self.value
    
    def activation(self) :
        x = sum([synapse.getValue() for synapse in self.prev_synapse]) + self.biais
        if self.isOutput :
            self.value = x
        else :
            self.value = 1/(1 + math.exp(-x))
    
    def propagate(self) :
        for synapse in self.next_synapse :
            synapse.activation()


class Synapse :
    
    def __init__(self, prevNeuron) :
        self.value = 0
        self.weight = random.random() * 2 - 1
        self.prev_neuron = prevNeuron
        self.error = 0
    
    def setWeight(self, weight) :
        self.weight = weight
    
    def getWeight(self) :
        return self.weight
    
    def getValue(self) :
        return self.value
    
    def activation(self) :
        self.value = self.prev_neuron.getValue() * self.weight



class Network :
    
    def __init__(self, layers) :
        n = len(layers)
        self.layers = [[Neuron() for _ in range(layers[layerIndex])] for layerIndex in range(n)]
        self.inputLayer = self.layers[0]
        self.outputLayer = self.layers[n-1]
        self.synapse = [[[Synapse(neuron) for _ in range(len(self.layers[layerIndex+1]))] for neuron in self.layers[layerIndex]] for layerIndex in range(n-1)]
        self.learningRate = 0.1
        self.batchSize = 128
        self.batch = []
        
        for neuronIndex in range(len(self.inputLayer)) :
            neuron = self.inputLayer[neuronIndex]
            neuron.setNextSynapse(self.synapse[0][neuronIndex])
        
        for layerIndex in range(1, n-1) :
            layer = self.layers[layerIndex]
            layerSize = len(layer)
            for neuronIndex in range(layerSize) :
                neuron = layer[neuronIndex]
                neuron.setNextSynapse(self.synapse[layerIndex][neuronIndex])
                previousLayerSize = len(self.layers[layerIndex - 1])
                neuron.setPrevSynapse([self.synapse[layerIndex-1][previousNeuronIndex][neuronIndex] for previousNeuronIndex in range(previousLayerSize)])
        
        for neuronIndex in range(len(self.outputLayer)) :
            neuron = self.outputLayer[neuronIndex]
            neuron.isOutput = True
            neuron.setPrevSynapse([self.synapse[n-2][previousNeuronIndex][neuronIndex] for previousNeuronIndex in range(len(self.layers[n-2]))])
    
    def propagate(self, state) :
        for i in range(len(self.inputLayer)) :
            neuron = self.inputLayer[i]
            neuron.setValue(state[i])
            neuron.propagate()
        
        for layer in self.layers[1:] :
            for neuron in layer :
                neuron.activation()
                neuron.propagate()
        
        res = []
        for neuron in self.outputLayer :
            res.append(neuron.getValue())
        
        return res
    
    
    
    def learn(self, data) :
        for experiment in data :
            self.propagate(experiment[0])
            for i in range(len(self.outputLayer)) :
                neuron = self.outputLayer[i]
                expectedResult = experiment[1][i]
                neuron.error = (neuron.value - expectedResult)
            
            for layerIndex in range(len(self.layers) - 2, -1, -1) :
                for neuronIndex in range(len(self.layers[layerIndex])) :
                    neuron = self.layers[layerIndex][neuronIndex]
                    
                    nextError = 0
                    for nextNeuronIndex in range(len(self.layers[layerIndex + 1])) :
                        nextError += self.layers[layerIndex + 1][nextNeuronIndex].error * self.synapse[layerIndex][neuronIndex][nextNeuronIndex].weight
                    neuron.error = neuron.value * (1 - neuron.value) * nextError
            
            for neuron in self.outputLayer :
                neuron.biais = neuron.biais - self.learningRate * neuron.error
            
            for layerIndex in range(len(self.layers) -1) :
                for neuronIndex in range(len(self.layers[layerIndex])) :
                    neuron = self.layers[layerIndex][neuronIndex]
                    
                    neuron.biais = neuron.biais - self.learningRate * neuron.error
                    
                    for nextNeuronIndex in range(len(self.layers[layerIndex + 1])) :
                        nextNeuron = self.layers[layerIndex + 1][nextNeuronIndex]
                        synapse = self.synapse[layerIndex][neuronIndex][nextNeuronIndex]
                        
                        synapse.weight = synapse.weight - self.learningRate * neuron.value * nextNeuron.error
    
    
    
    
    def learn_FOR_BATCH(self, data) :
        self.batch.append(data)
        if len(self.batch) >= self.batchSize :
            self.batchLearn(self.batch)
            self.batch = []
        
    
    def batchLearn(self, data) :
        self.reset_errors()
        n = len(data)
        
        k = -1
        for experiment in data :
            k += 1
            self.propagate(experiment[0])
            for i in range(len(self.outputLayer)) :
                neuron = self.outputLayer[i]
                expectedResult = experiment[1][i]
                neuron.error.append(neuron.value - expectedResult)
            
            for layerIndex in range(len(self.layers) - 2, -1, -1) :
                for neuronIndex in range(len(self.layers[layerIndex])) :
                    neuron = self.layers[layerIndex][neuronIndex]
                    
                    nextError = 0
                    for nextNeuronIndex in range(len(self.layers[layerIndex + 1])) :
                        nextError += self.layers[layerIndex + 1][nextNeuronIndex].error[k] * self.synapse[layerIndex][neuronIndex][nextNeuronIndex].weight
                    neuron.error.append(neuron.value * (1 - neuron.value) * nextError)
                    
                    for nextNeuronIndex in range(len(self.layers[layerIndex + 1])) :
                        nextNeuron = self.layers[layerIndex + 1][nextNeuronIndex]
                        synapse = self.synapse[layerIndex][neuronIndex][nextNeuronIndex]
                        synapse.error.append(neuron.value * nextNeuron.error[k])
            
        self.calculate_errors(n)
            
        for neuron in self.outputLayer :
            neuron.biais = neuron.biais - self.learningRate * neuron.error
            
        for layerIndex in range(len(self.layers) -1) :
            for neuronIndex in range(len(self.layers[layerIndex])) :
                neuron = self.layers[layerIndex][neuronIndex]
                    
                neuron.biais = neuron.biais - self.learningRate * neuron.error
                    
                for nextNeuronIndex in range(len(self.layers[layerIndex + 1])) :
                    nextNeuron = self.layers[layerIndex + 1][nextNeuronIndex]
                    synapse = self.synapse[layerIndex][neuronIndex][nextNeuronIndex]
                        
                    synapse.weight = synapse.weight - self.learningRate * synapse.error
    
                        
    def reset_errors(self) :
        for layerIndex in range(len(self.layers)) :
            for neuronIndex in range(len(self.layers[layerIndex])) :
                neuron = self.layers[layerIndex][neuronIndex]
                neuron.error = []
        
        for layerIndex in range(len(self.layers) - 1) :
            for neuronIndex in range(len(self.layers[layerIndex])) :
                for nextNeuronIndex in range(len(self.layers[layerIndex + 1])) :
                    synapse = self.synapse[layerIndex][neuronIndex][nextNeuronIndex]
                    synapse.error = []
    
    
    def calculate_errors(self, divider) :
        for layerIndex in range(len(self.layers)) :
            for neuronIndex in range(len(self.layers[layerIndex])) :
                neuron = self.layers[layerIndex][neuronIndex]
                neuron.error = sum(neuron.error) / divider
        
        for layerIndex in range(len(self.layers) - 1) :
            for neuronIndex in range(len(self.layers[layerIndex])) :
                for nextNeuronIndex in range(len(self.layers[layerIndex + 1])) :
                    synapse = self.synapse[layerIndex][neuronIndex][nextNeuronIndex]
                    synapse.error = sum(synapse.error) / divider


class DQN(Opponent) :
    
    
    __ANN = Network([9, 4, 8, 8, 4, 9])
    
    
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
        processed = self._linearState(state)
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
        initialState = self._linearState(state)
        finalState = self._linearState(newState)
        
        nextAction = self.__greedyPolicy(finalState)
        calculatedCumulativeReward = reward + self.__discountFactor * DQN.__ANN.propagate(finalState)[nextAction]
        
        expectations = DQN.__ANN.propagate(initialState)
        expectedCumulativeReward = expectations[action]
        error = calculatedCumulativeReward - expectedCumulativeReward
        
        target = expectations
        target[action] = expectedCumulativeReward + self.__learningRate * error
        
        DQN.__ANN.learn([(initialState, target)])
        
    
    @staticmethod
    def importQTable() :
        """
        Imports the QTable
        """
        pass
    
    @staticmethod
    def exportQTable() :
        """
        Exports the QTable
        """
        pass
    
    @staticmethod
    def resetQTable() :
        """
        Resets the QTable
        """
        pass

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
        if random.uniform(0, 1) <= self.__epsilon :
            return random.randint(0, 8)
        else :
            return self.__greedyPolicy(state)

