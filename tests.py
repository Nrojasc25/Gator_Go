import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def test1_addVertex(self):
        users = Graph()
        users.addVertex("User1")
        users.addVertex("User2")
        users.addVertex("User3")
        self.assertIn("User1", users.adjList)
        self.assertIn("User2", users.adjList)
        self.assertIn("User3", users.adjList)

    def test2_addEdge(self):
        users = Graph()
        users.addVertex("User1")
        users.addVertex("User2")
        users.addVertex("User3")
        users.addEdge("User1", "User2")
        users.addEdge("User1", "User3")
        self.assertIn("User2", users.adjList["User1"])
        self.assertIn("User3", users.adjList["User1"])

    def test3_getNeighbors(self):
        users = Graph()
        users.addVertex("User1")
        users.addVertex("User2")
        users.addVertex("User3")
        users.addEdge("User1", "User2") #undirected graph
        users.addEdge("User1", "User3")
        self.assertEqual(users.getNeighbors("User1"), ["User2", "User3"])
        self.assertEqual(users.getNeighbors("User2"), ["User1"])

if __name__ == '__main__':
    unittest.main()