from pprint import pprint


class GridWorldMDP:

    def __init__(self, initial_value=None, initial_policy=None):
        self.init_states()
        self.terminal_states = [(0, 0), (3, 3)]
        self.actions = {
            'UP': self.up,
            'DOWN': self.down,
            'LEFT': self.left,
            'RIGHT': self.right
        }

        if(not initial_value):
            self.value = [[0]*4]*4
        if(not initial_policy):
            self.policy = self.generate_initial_policy()

    def init_states(self):
        self.states = set()
        for x in range(0, 4):
            for y in range(0, 4):
                self.states.add((x, y))

    def generate_initial_policy(self):
        initial_policy = {}
        initial_states = [[0]*4]*4
        for index_x, state_x in enumerate(initial_states):
            for index_y, state_y in enumerate(initial_states):
                curr_state = (index_x, index_y)
                if(curr_state in self.terminal_states):
                    continue
                for action in self.actions:
                    if(curr_state not in initial_policy):
                        initial_policy[curr_state] = {
                            action: 0.25
                        }
                    else:
                        initial_policy[curr_state][action] = 0.25
        return initial_policy

    def states():
        pass

    def actions(state):
        self.actions

    def reward(state, action):
        if(state not in self.terminal_states):
            return -1
        else:
            return 0

    def policy():
        pass

    def value_function():
        pass

    def up(self, state):
        next_step = (state[0], state[1]-1)
        if(state in self.terminal_states or not self.in_bounds(next_step[0], next_step[1])):
            return state
        else:
            return next_step

    def down(self, state):
        next_step = (state[0], state[1]+1)
        if(state in self.terminal_states or not self.in_bounds(next_step[0], next_step[1])):
            return state
        else:
            return next_step

    def left(self, state):
        next_step = (state[0]-1, state[1])
        if(state in self.terminal_states or not self.in_bounds(next_step[0], next_step[1])):
            return state
        else:
            return next_step

    def right(self, state):
        next_step = (state[0]+1, state[1])
        if (state is self.terminal_states or not self.in_bounds(next_step[0], next_step[1])):
            return state
        else:
            return next_step

    def in_bounds(self, x, y):
        return x in range(0, 4) and y in range(0, 4)

    def __repr__(self):
        matrix = "\n"
        for row in self.value:
            matrix += ' '.join(map(str, row))+"\n"
        return matrix


mdp = GridWorldMDP()
print("**** Initial Policy for MDP ****")
pprint(mdp.policy)
print("**** Initial Value Function for MDP ****")
print(mdp)
print("Testing Actions")
print("Moving up from (1,1) : " + str(mdp.up((1, 1))))  # should be 1,0
print("Moving down from (1,1) : " + str(mdp.down((1, 1))))  # should be 1,0
print("Moving left from (1,1) : " + str(mdp.left((1, 1))))
print("Moving right from (1,1) : " + str(mdp.right((3, 1))))
