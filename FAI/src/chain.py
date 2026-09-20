class Chain:
    def __init__(self, states):
        self.states = states

    def valid(self):
        return all(self.states)
