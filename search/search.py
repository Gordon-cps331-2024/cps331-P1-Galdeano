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
from util import *
from Node import *


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
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
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


    fringe = Stack()
    node = Node(problem.getStartState(),0,None)
  
    if problem.isGoalState(problem.getStartState()):
        return node.getActions()
    
    #dictionary, stores position as the key, and cost as the value
    visited = {node.getState(): node.getCost()}
    fringe.push(node)

    while not fringe.isEmpty():
        node = fringe.pop()
        
        if problem.isGoalState(node.getState()):
            return node.getActions()

        for successor in problem.getSuccessors(node.getState()):
            
            if not successor[0] in visited or node.getCost() + successor[2] < visited[successor[0]]:
                
                visited[successor[0]] =  node.getCost() + successor[2]

                actions = list(node.getActions())
                actions.append(successor[1])
                
                s = Node(successor[0],node.getCost() + successor[2],actions)
                fringe.push(s)
                
          
    return False



    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    fringe = Queue()
    node = Node(problem.getStartState(),0,None)

    if not isinstance(node.getState()[1], set):

        if problem.isGoalState(problem.getStartState()):
            return node.getActions()
        
        #dictionary, stores position as the key, and cost as the value
        visited = {node.getState(): node.getCost()}
        fringe.push(node)

        while not fringe.isEmpty():
            node = fringe.pop()

            if problem.isGoalState(node.getState()):
                return node.getActions()
            
            for successor in problem.getSuccessors(node.getState()):
                
                if not successor[0] in visited or node.getCost() + successor[2] < visited[successor[0]]:
                    
                    visited[successor[0]] =  node.getCost() + successor[2]

                    actions = list(node.getActions())
                    actions.append(successor[1])
                    
                    s = Node(successor[0],node.getCost() + successor[2],actions)
                    fringe.push(s)
                    
            
        return []
    
    #for corners:
    else:

        if problem.isGoalState(problem.getStartState()):
            return node.getActions()
        
        visited = []
        visited.append(node.getState())

        fringe.push(node)


        while not fringe.isEmpty():
            node = fringe.pop()

            if problem.isGoalState(node.getState()):
                return node.getActions()
            
            for successor in problem.getSuccessors(node.getState()):
                
                if not successor[0] in visited:
                    
                    visited.append(successor[0])

                    actions = list(node.getActions())
                    actions.append(successor[1])
                    
                    s = Node(successor[0],node.getCost() + successor[2],actions)
                    fringe.push(s)
           
        return []
         
    

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    fringe = PriorityQueue()
    node = Node(problem.getStartState(),0,None)
  
    if problem.isGoalState(problem.getStartState()):
        return node.getActions()
    
    #dictionary, stores position as the key, and cost as the value
    visited = {node.getState(): node.getCost()}
    fringe.push(node,node.getCost())

    while not fringe.isEmpty():
        node = fringe.pop()

        if problem.isGoalState(node.getState()):
            return node.getActions()

        for successor in problem.getSuccessors(node.getState()):
            
            if not successor[0] in visited or node.getCost() + successor[2] < visited[successor[0]]:
                
                visited[successor[0]] =  node.getCost() + successor[2]

                actions = list(node.getActions())
                actions.append(successor[1])
                
                s = Node(successor[0],node.getCost() + successor[2],actions)
                fringe.push(s,s.getCost())
                
          
    return []


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #fringe is priority queue
    fringe = PriorityQueue()
    node = Node(problem.getStartState(),0,None)
    
    #this if is to verify if it is the corners problem or not
    if not isinstance(node.getState()[1], set):

        #if it is NOT corner problem:
        if problem.isGoalState(problem.getStartState()):
            return node.getActions()
        
        #visited stores already visited states
        visited = {node.getState(): node.getCost()}
        
        #pushes starter state
        fringe.push(node,heuristic(node.getState(),problem))

        while not fringe.isEmpty():
            node = fringe.pop()

            if problem.isGoalState(node.getState()):
                return node.getActions()

            for successor in problem.getSuccessors(node.getState()):
                
                #verifies if state has already been visited
                if not successor[0] in visited or node.getCost() + successor[2] < visited[successor[0]]:
                    
                    visited[successor[0]] =  node.getCost() + successor[2]

                    #stores actions to get to this state
                    actions = list(node.getActions())
                    actions.append(successor[1])
                  
                    #pushes successor to the fringe
                    s = Node(successor[0],node.getCost() + successor[2],actions)
                    fringe.push(s,s.getCost() + heuristic(successor[0],problem))
    
        return []
    
    else:
        #if it IS corner problem
        if problem.isGoalState(problem.getStartState()):
            return node.getActions()
        
        #visited stores already visited states
        visited = []
        visited.append(node.getState())

        #pushes starter state
        fringe.push(node,heuristic(node.getState(),problem))


        while not fringe.isEmpty():

            node = fringe.pop()
            
            if problem.isGoalState(node.getState()):
                return node.getActions()

            for successor in problem.getSuccessors(node.getState()):

                #verifies if state has already been visited
                if not successor[0] in visited:
                    
                    visited.append(successor[0])

                    #stores actions to get to this state
                    actions = list(node.getActions())
                    actions.append(successor[1])
                   
                    s = Node(successor[0],node.getCost() + successor[2],actions)

                    #verifies if corner heuristic is consistent, if it isnt, prints out INCONSISTENT
                    if heuristic(node.getState(),problem) > 1 + heuristic(successor[0],problem):
                        print("INCONSISTENT ")   
                        
                    #pushes successor to the fringe
                    fringe.push(s,s.getCost() + heuristic(successor[0],problem))
           
        return []
         
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
