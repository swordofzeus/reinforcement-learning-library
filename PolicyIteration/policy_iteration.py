import math
from pprint import pprint
from mdp.gridworld.grid_world_mdp import GridWorldMDP

class PolicyIteration():
    ''' 
        Implementation of Policy Iteration Reinforcement Learning Algorithm.
        Used for Planning Problems - when full dynamics of a system are known.
        @author ashish juneja
        @author jai kumar 
    '''

    def __init__(self, mdp):
        self.mdp = mdp
        self.bellman_error = 0

    def update_value_function(self):
        pass

    def evaluate_policy(self):
        current_policy = self.mdp.policy
        current_value_function = self.mdp.value_function
        for state in self.mdp.states:
            pprint(state)

    def improve_policy(self):
        pass

    def iterate(self):
        while(self.bellman_error > self.max_error):
            new_value_function = self.evaluate_policy(self.mdp)
            new_policy = self.improve_policy(new_value_function)
            self.mdp.policy = new_policy
            self.bellman_error = self.mdp.value_function - new_value_function


if __name__ == "__main__":
    mdp = GridWorldMDP()
    policy = PolicyIteration(mdp).evaluate_policy()
