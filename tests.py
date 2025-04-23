from datetime import datetime
import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    # add users, check they exist
    def test1_insertUser(self):
        g = Graph()
        g.insert("user1", [], "Jacksonville", 20250801, "000001")
        g.insert("user2", [], "orlando", 20250801, "000002")
        g.insert("user3", [], "miami", 20250801, "000003")
        g.insert("user4", [], "ocala", 20250801, "000004")
        self.assertIn("user1", g.users)
        self.assertIn("user2", g.users)
        self.assertIn("user3", g.users)
        self.assertEqual(g.searchUsername("user1"), True)

    # add user data, access it
    def test2_accessUserData(self):
        g = Graph()
        g.insert("user1", ["user2", "user3"], "Jacksonville", 20250801, "000001")
        g.insert("user2", ["user1", "user3"], "orlando", 20250801, "000002")
        g.insert("user3", ["user2"], "miami", 20250801, "000003")

        self.assertEqual(g.getFriends("user1"), ["user2", "user3"])
        self.assertEqual(g.getDestination("user2"), "orlando")
        self.assertEqual(int(g.getDate("user3").strftime("%Y%m%d")), 20250801)

    # # search friends and num of friend's friends with similar travel dates and same destination
    # def test3_getFriends(self):
    #     g = Graph()
    #     g.insert("user1", ["user2", "user3", "user4"], "dest", 20250805, "000001")
    #     g.insert("user2", ["user1", "user4"], "dest", 20250807, "000002")
    #     g.insert("user3", ["user1"], "dest", 20250804, "000003")
    #     g.insert("user4", ["user1", "user2"], "dest", 20250808, "000003")

    #     self.assertEqual(g.searchFriends("user1"), ["user2", "user3"])
    #     self.assertEqual(g.searchNumFriends("user2"), 1)

    def test4_DFSandBFS(self):
        g = Graph()
        g.insert("user1", ["user2", "user3", "user4"], "dest", 20250805, "000001")
        g.insert("user2", ["user1", "user4"], "dest", 20250807, "000002")
        g.insert("user3", ["user1"], "dest", 20250804, "000003")
        g.insert("user4", ["user1", "user2"], "dest", 20250808, "000003")

        # d = datetime.strptime(str(20250805), "%Y%m%d").date()
        # self.assertEqual(g.bfs("dest", d, "user1", 2), [])
        # self.assertEqual(g.dfs(), [])

        self.assertEqual(g.dfs("user1", 5, 2), [])

if __name__ == '__main__':
    unittest.main()
