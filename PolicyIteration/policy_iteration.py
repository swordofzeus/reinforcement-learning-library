import math


class PolicyIteration():
    ''' 
        Implementation of Policy Iteration Reinforcement Learning Algorithm.
        Used for Planning Problems - when full dynamics of a system are known.
        @author ashish juneja
        @author jai kumar 
    '''

    def __init__(self, mdp, transition_probability, reward_function, initial_value_estimate, convergence_error):
        self.mdp = mdp
        self.value_function = initial_value_estimate
        self.bellman_error = [number_of_states * math.infinity]

    def update_value_function(self):
        pass

    def evaluate_policy(self):
        pass

    def improve_policy(self):
        pass

    def iterate(self):
        while(self.bellman_error > self.max_error):
            new_value_function = self.evaluate_policy(self.mdp)
            new_policy = self.improve_policy(new_value_function)
            self.mdp.policy = new_policy
            self.bellman_error = self.mdp.value_function - new_value_function


if __name__ == "__main__":
    pass
