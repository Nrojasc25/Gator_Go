class Graph:
    def __init__(self):
        self.users = {} #name ,id
        self.friends = [] #list of friends
        self.destination = [] #list of destinations
        self.date = [] #list of dates

    def getFriends(self, user) -> list:
        return self.friends[self.users[user]]

    def getDestination(self, user):
        return self.destination[self.users[user]]

    def getDate(self, user):
        return self.date[self.users[user]]

    def insert(self, name, friends, destination, date):
        if name not in self.users: #check if user is already in system
            self.users[name] = len(self.users)
            for friend in friends:
                if friend not in self.users:
                    self.users[friend] = len(self.users)
                    self.friends[self.users[name]].append(self.users[friend])
            self.friends.append(friends)
            self.destination.append(destination)
            self.date.append(date)

    def addFriend(self, name, friend) -> bool:
        if name not in self.users:
            return False
        if friend not in self.users:
            self.users[friend] = len(self.users)
        self.friends[self.users[name]].append(self.users[friend]);
        return True

    def removeFriend(self, name, friend) -> bool:
        if name not in self.users or friend not in self.users:
            return False
        self.friends[self.users[name]].remove(self.users[friend])

    def bfs(self, dest, date, user) -> list:
        #destination string size int user string
        q = []
        visited = set()
        out = []
        q.append(self.users[user])
        visited.add(self.users[user])

        while q:
            cur = q.pop()
            if cur not in visited:
                if self.destination[cur] == dest and self.date[cur] == date:
                    out.append(cur)
                for friend in self.friends[cur]:
                    if friend not in visited and friend not in out:
                        q.append(friend)
        return out

    def dfs(self, dest, date, user) -> list:
        # destination: string, date: int, user: string
        visited = set()
        out = []
        stack = [self.users[user]]

        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                if self.destination[cur] == dest and self.date[cur] == date:
                    out.append(cur)
                for friend in reversed(self.friends[cur]): #mimic stack behavior
                    if friend not in visited and friend not in out:
                        stack.append(friend)
        return out
