class Graph:
    def __init__(self):
        # this won't work. Other class for User??
        self.users = {} #name ,id 
        self.friends = [] #list of friends 
        self.destination = [] #list of destinations 
        self.date = [] #list of dates 
    
    # insert(userID, userName, destination travelDate)
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

    # user, friend
    def addFriend(self, name, friend) -> bool: #undirected graph
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

    # self (unnecessary parameters dest, date, what is user??)
    # do we need bfs/dfs?? should we compare data structure or search algorithm instead?? 

    # returns list of friends by their userIDs that have same dest and similar date (+-2 days)
    def searchFriends(self, dest, date):
        pass

    # returns number of friends that have same dest and similar date (+-2 days)
    def searchNumFriends(self, dest, data):
        pass

    # HELPER FUNCTIONS

    # returns user's user name
    def getUserName(self, user):
        pass

    # returns user's destination 
    def getDestination(self, user):
        pass
    
    # returns user's date of travel
    def getTravelDate(self, user):
        pass

    def bfs(self, dest, date, user) -> list:
        #destination string size int user string
        q = []
        visited = []
        out = []
        q.append(self.users[user])
        visited.append(self.users[user])
        while len(q) > 0:
            cur = q.popleft()
            for friend in self.friends[cur]:
                if friend not in visited and friend not in out:
                    q.append(friend)
            if self.destination[cur] == dest and self.date[cur] == date:
                out.append(cur)
        return out
    
    def getBFSTime(self):
        pass
    
    def dfs(self, dest, date, user):
        pass

    def getDFSTime(self):
        pass
    
    # this won't work yet, might need to change based on restructure
    def test(self):
        outputList = []
        for user in self.friends:
            outputList.append(f"{user} -> {' '.join(self.friends[user])}")
        return outputList
    
    # FUNCTIONS FOR PROGRAM RUN

    def tempInsert(self, user): #testing something, remove later
        self.users[0] = user
        
    # returns true if user exists
    def searchUserName(self, userName):
        return userName in self.users.values()
    
    def searchResults(self, user):
        # from given user, return all friends that go to the same location on similar date
        # print the search times (DFS vs BFS). ?? unless we change this
        pass
