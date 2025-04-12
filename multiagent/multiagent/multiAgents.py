# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        score = successorGameState.getScore()

        for ghostState, scaredTime in zip(newGhostStates, newScaredTimes):
            ghostPos = ghostState.getPosition()
            distToGhost = manhattanDistance(newPos, ghostPos)
            if scaredTime > 0:
                score = score + 200
                score = score / (distToGhost + 1)
            elif distToGhost < 2:
                score = score - 1000

        foodList = newFood.asList()
        if foodList:
            dist = []
            for food in foodList:
                dist.append(manhattanDistance(newPos, food))
            closestFoodDist = min(dist)
            score += 10 / (closestFoodDist + 1)
        if action == Directions.STOP:
            score = score - 50
        foodEaten = currentGameState.getFood().count() - newFood.count()
        if foodEaten > 0:
            score = score + 100

        return score


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, game_state: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        actions = game_state.getLegalActions(0)
        maximum_result = float('-inf')

        for a in actions:
            successor = game_state.generateSuccessor(0, a)
            currentResult = self.minValue(successor, 0, 1)
            if currentResult > maximum_result:
                maximum_result = currentResult
                max_action_pacman = a
        return max_action_pacman

    def minValue(self, game_state, depth, agent_current):
        if game_state.isLose() or depth == self.depth or game_state.isWin():
            return self.evaluationFunction(game_state)

        actions = game_state.getLegalActions(agent_current)
        agents = game_state.getNumAgents()

        if agent_current < agents - 1:
            return min(map(lambda a: self.minValue(game_state.generateSuccessor(agent_current, a), depth, agent_current + 1),
                           actions))
        else:
            return min(map(lambda a: self.maxValue(game_state.generateSuccessor(agent_current, a), depth + 1), actions))

    def maxValue(self, gameState, depth):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)

        actions = gameState.getLegalActions(0)
        return max(map(lambda a: self.minValue(gameState.generateSuccessor(0, a), depth, 1), actions))

        # util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, game_state: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        actions = game_state.getLegalActions(0)
        maximum = float('-inf')

        alpha = float('-inf') #cel mai bun rezultat pe care agentul maxim (Pacman) il poate garanta pana la acel moment
        beta = float('inf')   #cel mai bun rezultat pe care agentul minim (Pacman) il poate garanta pana la acel moment

        for a in actions:
            successor = game_state.generateSuccessor(0, a)

            val_current = self.minValue(successor, 0, 1, alpha, beta)
            if maximum < val_current:
                maximum = val_current
                max_action_pacman = a
                alpha = max(alpha, val_current)
        return max_action_pacman

    def maxValue(self, game_state, depth, alpha, beta):
        if game_state.isWin() or depth == self.depth or game_state.isLose():
            return self.evaluationFunction(game_state)
        actions = game_state.getLegalActions(0)
        maximum_value = float('-inf')
        for action in actions:
            successor = game_state.generateSuccessor(0, action)

            maximum_value = max(maximum_value, self.minValue(successor, depth, 1, alpha, beta))
            if maximum_value > beta:
                return maximum_value
            alpha = max(alpha, maximum_value)
        return maximum_value

    def minValue(self, game_state, depth, agent_current,alpha, beta):
        if game_state.isWin() or game_state.isLose() or depth == self.depth:
            return self.evaluationFunction(game_state)
        actions = game_state.getLegalActions(agent_current)
        minimum_value = float('inf')
        agents = game_state.getNumAgents()
        for action in actions:
            successor = game_state.generateSuccessor(agent_current, action)
            if agent_current < agents - 1:

                minimum_value = min(minimum_value, self.minValue(successor, depth, agent_current + 1, alpha, beta))
            else:
                minimum_value = min(minimum_value, self.maxValue(successor, depth + 1, alpha, beta))
            if minimum_value < alpha:
                return minimum_value
            beta = min(beta, minimum_value)
        return minimum_value

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, game_state: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        actions = game_state.getLegalActions(0)
        max_result = float('-inf')
        for a in actions:
            successor = game_state.generateSuccessor(0, a)
            result_iterm = self.chanceExpect(successor, 0, 1)
            if result_iterm > max_result:
                max_result = result_iterm
                max_action_pacman = a
        return max_action_pacman

    def getMaxAction(self, game_state):
        actions = game_state.getLegalActions(0)
        if not actions:
            return 'Stop'

    def maxExpect(self, game_state, depth):
        if game_state.isWin() or game_state.isLose() or depth == self.depth:
            return self.evaluationFunction(game_state)

        actions = game_state.getLegalActions(0)
        successors = list(map(lambda a: game_state.generateSuccessor(0, a), actions))
        return max(self.chanceExpect(s, depth, 1) for s in successors)

    def chanceExpect(self, gameState, depth, agent_current):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
             return self.evaluationFunction(gameState)

        actions = gameState.getLegalActions(agent_current)
        successors = list(map(lambda a: gameState.generateSuccessor(agent_current, a), actions))

        if agent_current < gameState.getNumAgents() - 1:
            return sum(self.chanceExpect(s, depth, agent_current + 1) for s in successors) / len(successors)
        else:
            return sum(self.maxExpect(s, depth + 1) for s in successors) / len(successors)

        # util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    position= currentGameState.getPacmanPosition()

    food_positions = currentGameState.getFood().asList()
    ghost_positions = currentGameState.getGhostPositions()

    capsules_positions = currentGameState.getCapsules()

    state_of_ghost = currentGameState.getGhostStates()
    scared_g = [ghost.scaredTimer for ghost in state_of_ghost]

    food_remaining = len(food_positions)
    capsules_remaining = len(capsules_positions)
    scared= list()
    enemy = list()

    enemy_position = list()
    scared_position = list()

    eval = currentGameState.getScore()

    distance_from_food = [manhattanDistance(position, food_position) for food_position in food_positions]
    if len(distance_from_food) is not 0:
        closest_food = min(distance_from_food)
        eval -= 1.0 * closest_food

    enemy = [g for g in state_of_ghost if g.scaredTimer]
    scared = [g for g in state_of_ghost if not g.scaredTimer]

    for s in scared:
        scared_position.append(s.getPosition())

    for e in enemy:
        enemy_position.append(e.getPosition())

    if len(scared_position):
        distance_from_scared_ghost = list(map(lambda scared_ghost_position: manhattanDistance(position, scared_ghost_position), scared_position))
        scared_close = min(distance_from_scared_ghost)
        eval = eval - 3.0 * scared_close


    if len(enemy_position):
        distance_enemy = list(map(lambda e: manhattanDistance(position, e), enemy_position))
        enemy_close = min(distance_enemy)
        eval -= 2.0 * (1 / enemy_close)

    penalty = 20.0 * capsules_remaining + 4.0 * food_remaining
    eval -= penalty

    return eval
    # util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
