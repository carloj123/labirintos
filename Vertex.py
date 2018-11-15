class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()
#<circle cy="7.5" cx="0.5" r="0.2" stroke="red" fill="red" />