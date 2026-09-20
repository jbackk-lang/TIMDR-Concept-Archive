class Horizon:
    def __init__(self):
        self.hidden = []

    def hide(self, x):
        self.hidden.append(x)

    def reveal(self):
        return self.hidden
