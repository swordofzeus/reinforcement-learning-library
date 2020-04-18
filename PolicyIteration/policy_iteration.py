import math
import copy
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

    def one_step_lookahead(self, state):
        updated_value = 0
        for action in self.mdp.actions:
            new_state = self.mdp.actions[action](state)
            value_of_new_state = self.mdp.value[new_state[0]][new_state[1]]
            updated_value += self.mdp.policy[state][action] * \
                (self.mdp.reward(new_state, action)+value_of_new_state)

        return updated_value

    def evaluate_policy(self):
        current_policy = self.mdp.policy
        current_value_function = copy.deepcopy(self.mdp.value)
        for state in self.mdp.states:
            if(state in self.mdp.terminal_states):
                continue
            new_value = self.one_step_lookahead(state)
            current_value_function[state[0]][state[1]] = new_value
        pprint(current_value_function)
        return current_value_function

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
    for i in range(0, 10):
        new_value_function = PolicyIteration(mdp).evaluate_policy()
        mdp.value = new_value_function

    # mdp.value = new_value_function
    # new_value_function = PolicyIteration(mdp).evaluate_policy()
    # mdp.value = new_value_function
    # new_value_function = PolicyIteration(mdp).evaluate_policy()
