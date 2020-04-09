from pprint import pprint
class GridWorldMDP:

    def __init__(self,initial_value=None,initial_policy=None):
        self.states = [[0]*4]*4
        self.terminal_states = [(0,0),(3,3)]
        self.actions = {
            'UP': self.up,
            'DOWN': self.down,
            'LEFT': self.left,
            'RIGHT': self.right
        }
        
        if(not initial_value):
            self.value = self.states
        if(not initial_policy):
            self.policy = self.generate_initial_policy()
    
    def generate_initial_policy(self):
        initial_policy={}
        initial_states = [[0]*4]*4
        for index_x,state_x in enumerate(initial_states):
            for index_y,state_y in enumerate(initial_states):
                for action in ['UP','DOWN','LEFT','RIGHT']:
                    curr_state = (index_x,index_y)
                    if(curr_state not in initial_policy):
                        initial_policy[curr_state] = {
                            action:0.25
                        }
                    else:
                        initial_policy[curr_state][action] = 0.25
        return initial_policy


    def states():
        pass

    def actions(state):
        self.actions

    def reward(state,action):
        if(state not in self.terminal_states):
            return -1
        else:
            return 0

    def policy():
        pass

    def value_function():
        pass

    def up(self,state):
        if(state in self.terminal_states):
            return state
        else:
            next_step = (state[0],state[1]+1)
            if(next_step[1] in range(0,3)):
                return next_step
            else:
                return state

    def down(self,state):
        pass

    def left(self,state):
        pass

    def right(self,state):
        pass

    def __repr__(self):
        matrix = "\n"
        for row in self.states:
            matrix += ' '.join(map(str,row))+"\n"
        return matrix   


#pprint(initial_policy)
#initial_value = [[0]*4]*4
mdp = GridWorldMDP()
pprint(mdp.policy)
print(mdp)
