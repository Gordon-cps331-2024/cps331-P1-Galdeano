class Node:
    def __init__(self, state, cost, actions=None):
        self.state = state
        #cost to get to this state
        self.cost = cost
        #actions to get to this state
        self.actions = actions if actions is not None else []

    def getState(self):
        return self.state
    
    def getActions(self):
        return self.actions
    
    def getCost(self):
        return self.cost
    
