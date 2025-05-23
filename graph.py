from datetime import timedelta
from User import user
import time
from collections import deque

class Graph:
    def __init__(self):
        self.users = {} #username, user
        self.id_to_user_object = {}

    def insert(self, username, friends, destination, date, id): #insert function for new user
        if username not in self.users: #check if user is already in system
            newUser = user(username, friends, destination, date, id)
        ID = str(id).zfill(6) # formatted leading zeros
        if ID not in self.id_to_user_object: #check if user is already in system
            newUser = user(username, friends, destination, date, ID)
            self.users[username] = newUser
            self.id_to_user_object[ID] = newUser


    def getFriends(self, username) -> list: #returns friends list of user
        return self.users[username].getFriends()
    
    def getDestination(self, username): #returns destination of user
        return self.users[username].getDestination()
    
    def getDate(self, username): #returns date of user
        return self.users[username].getDate()
    
    # returns true if user exists
    def searchUsername(self, username):
        return username in self.users
    
    def getID(self, username):
        return self.users[username].getID()
    
    def bfs(self, dest, date, user, n, max_users=5) -> list:
        visited = set()
        out = []
        q = []

        # Date window for filtering
        low, high = date - timedelta(days=n), date + timedelta(days=n)
        q.append(self.users[user])

        while q and len(out) <= max_users: #loop while there are still users to search or until out == n
            cur = q.pop(0) #cur is a user object
            if cur.getUsername() not in visited: #check if already visited
                visited.add(cur.getUsername())
                if cur.getDestination() == dest and low <= cur.getDate() <= high:
                    out.append(cur.getUsername())
                for friend in cur.getFriends():
                    if self.id_to_user_object[friend].getUsername() not in visited:
                        q.append(self.id_to_user_object[friend])
        if user in out:
            out.remove(user)
        return out
    
    def getBFSTime(self, dest, date, user, n, max_users):
        from time import perf_counter
        start = perf_counter()
        result = self.bfs(dest, date, user, n, max_users)
        end = perf_counter()
        elapsed = end - start
        return result, elapsed

    
    def dfs(self, dest, date, user, n, max_users=5) -> list:
        visited = set()
        out = []
        q = []

        # Date window for filtering
        low, high = date - timedelta(days=n), date + timedelta(days=n)
        q.append(self.users[user])

        while q and len(out) <= max_users:  # looop while there are still users to search or until out == n
            cur = q.pop(-1)  # cur is a user object
            if cur.getUsername() not in visited:  # check if already visited
                visited.add(cur.getUsername())
                if cur.getDestination() == dest and low <= cur.getDate() <= high:
                    out.append(cur.getUsername())
                for friend in cur.getFriends():
                    if self.id_to_user_object[friend].getUsername() not in visited:
                        q.append(self.id_to_user_object[friend])

        if user in out:
            out.remove(user)
        return out

    def getDFSTime(self, dest, date, user, n, max_users):
        from time import perf_counter
        start = perf_counter()
        result = self.dfs(dest, date, user, n, max_users)
        end = perf_counter()
        elapsed = end - start
        return result, elapsed


    # prints search results and time of search for BFS vs DFS
    def printSearchResults(self, user):
        from datetime import datetime

        dest = self.getDestination(user)
        date_int = self.getDate(user)
        date_obj = datetime.strptime(str(date_int), "%Y%m%d").date()
        max_results = 5  # Or make this a parameter if needed

        print(f"\nSearching for friends of {user} going to {dest} around {date_obj.strftime('%Y-%m-%d')}...")

        bfs_results, bfs_time = self.getBFSTime(dest, date_obj, user, max_results)
        dfs_results, dfs_time = self.getDFSTime(dest, date_obj, user, max_results)

        print("\nBFS Results:")
        if bfs_results:
            for friend in bfs_results:
                travel_date = datetime.strptime(str(g.getDate(friend)), "%Y%m%d").date()
                print(f"{friend} (Travel Date: {travel_date.strftime('%Y-%m-%d')})")
        else:
            print("No rides found.")
        print(f"BFS Search Time: {bfs_time:.6f} seconds")

        print("\nDFS Results:")
        if dfs_results:
            for friend in dfs_results:
                travel_date = datetime.strptime(str(g.getDate(friend)), "%Y%m%d").date()
                print(f"{friend} (Travel Date: {travel_date.strftime('%Y-%m-%d')})")
        else:
            print("No rides found.")
        print(f"DFS Search Time: {dfs_time:.6f} seconds\n")



    # FUTURE WORK

    def addFriend(self, name, friend) -> bool: #adds a friend to a user
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].addFriend(friend)

    def removeFriend(self, name, friend) -> bool: #removes a friend
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].removeFriend(friend)

    
    # FUNCTIONS FOR PROGRAM RUN

    def tempInsert(self, user): #testing something, remove later
        self.users[0] = user
    
    def printSearchResults(self, user):
        # from given user, return all friends that go to the same location on similar date
        # print the search times (DFS vs BFS). ?? unless we change this
        pass



    
