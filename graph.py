class Graph:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self, vertex):
        pass

    def addEdge(self, v1, v2):
        pass

    def display(self):
        outputList = []
        for vertex in self.adj_list:
            outputList += (f"{vertex} -> {self.adj_list[vertex]}")
