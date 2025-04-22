from datetime import timedelta
from User import user

class Graph:
    def __init__(self):
        self.users = {} #username, user

    def insert(self, username, friends, destination, date, id): #insert function for new user
        ID = str(id).zfill(6) # formatted leading zeros
        if username not in self.users: #check if user is already in system
            newUser = user(username, friends, destination, date, ID)
            self.users[username] = newUser

    def getFriends(self, username) -> list: #returns friends list of user
        return self.users[username].getFriends()
    
    def getDestination(self, username): #returns destination of user
        return self.users[username].getDestination()
    
    def getDate(self, username): #returns date of user
        return self.users[username].getDate()
    
    def getFormattedDate(self, username):
        unformatted = self.getDate(username)
        return unformatted #format date to YYYY/MM/DD      
    
    def getID(self, username):
        return self.users[username].getID()
    
    # returns true if user exists
    def searchUsername(self, username):
        return username in self.users
    
    def bfs(self, dest, date, user, n) -> list: #currentl searches all users in a dataset
        #dest - destination to be visited
        #date - intended date of travel, needs to be datetime object
        #if not run datetime.strptime(str(date), "%Y%m%d").date() before passing
        #it turns the yyyymmdd int into a datetime object
        #user - user who is traveling
        #n - int indicating how fat from date of travel you can go
        q = []
        visited = set()
        out = []
        low, high = (date - timedelta(days=n), date + timedelta(days=n))
        q.append(self.users[user])

        while q:
            cur = q.pop(0)
            if cur not in visited:
                visited.add(cur)
                if cur.getDestination() == dest and low <= cur.getDate() <= high:
                    out.append(cur.getUsername())
                for friend in cur.getFriends():
                    if friend not in visited and friend not in out:
                        q.append(self.users[friend])

        out.remove(user)
        return out

    # # returns list of friend usernames that have same dest and similar date (+-2 days)
    # # !! change date format on user's set date so that sum works for different months.
    # def searchFriends(self, username) -> list:
    #     friends = self.getFriends(username)
    #     dest = self.users[username].getDestination()
    #     date = self.users[username].getDate()
    #     output = []
    #     for i in range(0, len(friends)):
    #         if self.users[friends[i]].getDestination() == dest:
    #             if abs(self.users[friends[i]].getDate() - date) <= 2:
    #                 output.append(friends[i])
    #     return output

    # # returns number of friends that have same dest and similar date (+-2 days)
    # def searchNumFriends(self, username):
    #     return len(self.searchFriends(username)) - 1 # assuming nondirected graph
    
    def getBFSTime(self):
        pass
    
    def dfs(self, dest, date, user, n) -> list:
        stack=[]
        visited=set()
        out=[]
        low, high= (date-timedelta(days=n), date+timedelta(days=n))
        stack.append(self.users[users])

        while stack:
            cur=stack.pop()
            if cur not in visited:
                visited.add(cur)
                if cur.getDestination()==dest and low<=cur.getDate() <=high:
                    out.append(cur)
                for friend in cur.getFriends:
                    if friend not in visited and friend not in out:
                        stack.append(friend)


        return out

    def getDFSTime(self):
        pass

    # prints search results and time of search for BFS vs DFS
    def printSearchResults(self, user):
        # from given user, return all friends that go to the same location on similar date
        # print the search times (DFS vs BFS). ?? unless we change this
        pass

    # FUTURE WORK

    def addFriend(self, name, friend) -> bool: #adds a friend to a user
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].addFriend(friend)

    def removeFriend(self, name, friend) -> bool: #removes a friend
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].removeFriend(friend)
