from collections import deque

from node import UserNode

class Graph:
    def __init__(self):
        self.users = {}  # name -> UserNode

    def insert(self, name, friends, destination, date):
        if name not in self.users:
            self.users[name] = UserNode(name, destination, date)
        else:
            self.users[name].destination = destination
            self.users[name].date = date

        for friend_name in friends:
            if friend_name not in self.users:
                self.users[friend_name] = UserNode(friend_name)
            self.users[name].add_friend(self.users[friend_name])
            self.users[friend_name].add_friend(self.users[name])  # Optional: mutual friendship

    def add_friend(self, name, friend):
        if name not in self.users:
            return False
        if friend not in self.users:
            self.users[friend] = UserNode(friend)
        self.users[name].add_friend(self.users[friend])
        self.users[friend].add_friend(self.users[name])  # Optional
        return True

    def remove_friend(self, name, friend):
        if name not in self.users or friend not in self.users:
            return False
        self.users[name].remove_friend(self.users[friend])
        self.users[friend].remove_friend(self.users[name])  # Optional
        return True

    def bfs(self, destination, date, start_name):
        if start_name not in self.users:
            return []

        start_node = self.users[start_name]
        visited = set()
        q = deque([start_node])
        visited.add(start_node)
        out = []

        while q:
            cur = q.popleft()
            if cur.destination == destination and cur.date == date:
                out.append(cur.name)
            for friend in cur.friends:
                if friend not in visited:
                    visited.add(friend)
                    q.append(friend)

        return out

    def dfs(self, destination, date, start_name):
        if start_name not in self.users:
            return []

        start_node = self.users[start_name]
        visited = set()
        stack = [start_node]
        out = []

        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            if cur.destination == destination and cur.date == date:
                out.append(cur.name)
            for friend in cur.friends:
                if friend not in visited:
                    stack.append(friend)

        return out


g = Graph()

# Create a small graph:
# Alice -- Bob -- David
#   |       |
# Charlie   Eva
#             \
#              Frank

g.insert("Alice", ["Bob", "Charlie"], "Paris", "2025-06-01")
g.insert("Bob", ["David", "Eva"], "London", "2025-06-01")
g.insert("Charlie", [], "Paris", "2025-06-01")
g.insert("David", [], "Paris", "2025-06-01")
g.insert("Eva", ["Frank"], "Paris", "2025-06-01")
g.insert("Frank", [], "Paris", "2025-06-01")

print("=== BFS Traversal ===")
bfs_result = g.bfs("Paris", "2025-06-01", "Alice")
print("Users going to Paris on 2025-06-01 (BFS):", bfs_result)

print("\n=== DFS Traversal ===")
dfs_result = g.dfs("Paris", "2025-06-01", "Alice")
print("Users going to Paris on 2025-06-01 (DFS):", dfs_result)
