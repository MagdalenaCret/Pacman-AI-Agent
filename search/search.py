# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions, Actions
from typing import List
from collections import deque

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        # util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        # util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        # util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    from typing import List

    class Directions:
        # Dummy Directions class for illustration purposes
        NORTH = "North"
        SOUTH = "South"
        EAST = "East"
        WEST = "West"

    class SearchProblem:
        # Dummy search problem class for illustration purposes
        def getStartState(self):
            raise NotImplementedError

        def isGoalState(self, state):
            raise NotImplementedError

        def getSuccessors(self, state):
            raise NotImplementedError

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
        """
        Search the deepest nodes in the search tree first.

        Your search algorithm needs to return a list of actions that reaches the
        goal. Make sure to implement a graph search algorithm.

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print("Start:", problem.getStartState())
        print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
        print("Start's successors:", problem.getSuccessors(problem.getStartState()))
        """

        path = []
        nodes = []

        node_to_start = problem.getStartState()
        stack_dfs = util.Stack()

        stack_dfs.push((node_to_start, path))

        while True and not problem.isGoalState(node_to_start):
            if stack_dfs.isEmpty():
                break
            node, path = stack_dfs.pop()
            if node not in nodes:
                if problem.isGoalState(node):  return path

                nodes.append(node)
                successors = problem.getSuccessors(node)
                pathc_dfs = [(s[0], path + [s[1]]) for s in successors]
                for item in pathc_dfs:
                    stack_dfs.push(item)

        return []
        # util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""

    path = []
    nodes = []

    node_to_start = problem.getStartState()
    queue_bfs = util.Queue()

    queue_bfs.push((node_to_start, path))

    while True and not problem.isGoalState(node_to_start):
        if queue_bfs.isEmpty():
            break
        node, path = queue_bfs.pop()

        if node not in nodes:
            if problem.isGoalState(node):  return path

            nodes.append(node)
            successor = problem.getSuccessors(node)
            pathc_bfs = [(s[0], path + [s[1]]) for s in successor]
            for item in pathc_bfs:
               queue_bfs.push(item)

    return []
    # util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""

    path = []
    nodes = []

    node_to_start = problem.getStartState()
    queue_ucs = util.PriorityQueue()

    queue_ucs.push((node_to_start, path, 0), 0)
    while True and not problem.isGoalState(node_to_start):
        if queue_ucs.isEmpty():
            break
        node, path, cost = queue_ucs.pop()

        if node not in nodes:
            if problem.isGoalState(node):  return path

            nodes.append(node)
            successor = problem.getSuccessors(node)
            pathc_ucs = [((s[0], path + [s[1]], cost + s[2]), cost + s[2]) for s in successor]
            for item, priority in pathc_ucs:
                 queue_ucs.push(item, priority)

    return []
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def reconstructpath_function(visited, start, goal):
    path = []
    while goal != start:
        parent, action = visited[goal][1], visited[goal][2]
        path.append(action)
        goal = parent
    return path[::-1]

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""

    start = problem.getStartState()
    visited = dict()
    visited[start] = (0, None, '')
    startQueue = util.PriorityQueue()
    startQueue.push(start, 0)
    open = []
    closed = []
    listA = {}
    open.append(start)
    listA[start] = 0
    while not startQueue.isEmpty():
        node = startQueue.pop()

        if problem.isGoalState(node):
            return reconstructpath_function(visited, start, node)

        for neighbor in problem.getSuccessors(node):      # succesori pentru fiecare vecin
            neighborPosition, direction, cost = neighbor

            # costul total
            costT = visited[node][0] + cost
            heuristic_value = heuristic(neighborPosition, problem)
            a = costT + heuristic_value

            if neighborPosition not in listA or listA[neighborPosition] > a:
                listA[neighborPosition] = a
                startQueue.update(neighborPosition, a)

                visited[neighborPosition] = (costT, node, direction)
        closed.append(node)

def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    startNode = problem.getStartState()

    if problem.isGoalState(startNode):
        return []

    frontier = util.PriorityQueue()
    path_Greedy = []
    exploredNodes = []
    frontier.push((startNode, path_Greedy), heuristic(startNode, problem))
    while not frontier.isEmpty():
        node, path = frontier.pop()

        if node not in exploredNodes:
            if problem.isGoalState(node):
                return path

            exploredNodes.append(node)

            successors = problem.getSuccessors(node)

            for child, action, cost in successors:

                heuristic_value = heuristic(child, problem)
                frontier.push((child, path + [action]), heuristic_value)
    # util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# search problema suplimentar - Greedy Best First Search
gbfs = greedyBestFirstSearch
