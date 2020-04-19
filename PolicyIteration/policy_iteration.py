import math
import copy
from pprint import pprint
import numpy as np
np.set_printoptions(precision=2)
from mdp.gridworld.grid_world_mdp import GridWorldMDP


class PolicyIteration():
    ''' 
        Implementation of Policy Iteration Reinforcement Learning Algorithm.
        Used for Planning Problems - when full dynamics of a system are known.
        @author ashish juneja
        @author jai kumar 
    '''

    def __init__(self, mdp,max_iter,bellman_tolerance):
        self.mdp = mdp
        self.max_iter = max_iter
        self.bellman_tolerance = bellman_tolerance
        self.bellman_error = 0

    def update_value_function(self):
        pass

    def one_step_lookahead(self, state):
        updated_value = 0
        for action in self.mdp.actions:
            '''Invoke an action, and determine a list of possible new states we can end up in'''
            possible_new_states = self.mdp.actions[action](state)
            for new_state in possible_new_states:
                '''Compute the value of the new state by using the Bellman Expectation Equation'''
                value_of_new_state = self.mdp.value[new_state[0]][new_state[1]]
                updated_value += self.mdp.policy[state][action] * \
                    self.mdp.transition_prbability(state,action,new_state)*(self.mdp.reward(new_state, action)+value_of_new_state)

        return updated_value

    def update_value_function(self):
        current_policy = self.mdp.policy
        current_value_function = copy.deepcopy(self.mdp.value)
        for state in self.mdp.states:
            if(state in self.mdp.terminal_states):
                continue
            new_value = self.one_step_lookahead(state)
            current_value_function[state[0]][state[1]] = new_value
        return current_value_function

    def improve_policy(self,new_value_function):
        return {}

    def find_optimal_policy(self):
        new_value_function = self.evaluate_policy()
        new_policy = self.improve_policy(new_value_function)

    def evaluate_policy(self):
        for i in range(0, self.max_iter):
            old_value_function = mdp.value
            new_value_function = self.update_value_function()
            
            bellman_error = np.max((np.subtract(old_value_function,new_value_function)))
            mdp.value = new_value_function
            
            print("MDP Value Function After Iteration {}:\n {}".format(i,mdp))
            if(bellman_error < self.bellman_tolerance):
                print("exiting early, bellman error is below tolerance")
                break
        
        return new_value_function

if __name__ == "__main__":
    mdp = GridWorldMDP()
    PolicyIteration(mdp,max_iter=100,bellman_tolerance=0.01).find_optimal_policy()