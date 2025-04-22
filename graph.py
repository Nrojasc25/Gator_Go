from datetime import timedelta
from User import user
import time
from collections import deque

class Graph:
    def __init__(self):
        self.users = {} #username, user
        self.id_to_user_object = {}

    def insert(self, username, friends, destination, date, id): #insert function for new user
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
    
    def getFormattedDate(self, username):
        unformatted = self.getDate(username)
        return unformatted #format date to YYYY/MM/DD      
    
    def getID(self, username):
        return self.users[username].getID()
    
    # returns true if user exists
    def searchUsername(self, username):
        return username in self.users
    
    def bfs(self, dest, date, user, n) -> list:
        from datetime import datetime, timedelta

        #q = []
        q=deque()
        visited = set()
        out = []

        low, high = (date - timedelta(days=n), date + timedelta(days=n))

        q.append(self.users[user])
        visited.add(user)

        while q:
            cur = q.popleft() #O(1) compared to pop()
            cur_username = cur.username
            user_date = datetime.strptime(str(cur.getDate()), "%Y%m%d").date()

            if cur_username != user and cur.getDestination() == dest and low <= user_date <= high:
                out.append((cur_username, user_date))

            for friend_id in cur.getFriends():
                friend_obj = self.id_to_user_object.get(friend_id)
                if friend_obj:
                    friend_username = friend_obj.username
                    if friend_username not in visited:
                        visited.add(friend_username)
                        q.append(friend_obj)

        # Sort by date and return top `n`
        out.sort(key=lambda x: x[1])
        return [username for username, _ in out[:n]]



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
    
    def getBFSTime(self, dest, date, user, n):
        start = time.time()
        result = self.bfs(dest, date, user, n)
        end = time.time()
        elapsed = end - start
        return result, elapsed

    
    def dfs(self, dest, date, user, n) -> list:
        stack=[]
        visited=set()
        out=[]
        low, high= (date-timedelta(days=n), date+timedelta(days=n))
        stack.append(self.users[user])


        while stack:
            cur=stack.pop()
            if cur not in visited:
                visited.add(cur)
                from datetime import datetime
                user_date = datetime.strptime(str(cur.getDate()), "%Y%m%d").date()
                if cur.username != user and cur.getDestination() == dest and low <= user_date <= high:
                    out.append(cur.username)
                    if len(out) >= n:
                        break

                for friend in cur.getFriends():
                    if friend not in visited and friend not in out:
                        friend_obj = self.id_to_user_object.get(friend)
                        if friend_obj:
                            stack.append(friend_obj)



        #return out
        out.sort(key=lambda username: datetime.strptime(str(self.getDate(username)), "%Y%m%d").date())
        return out[:n]


    def getDFSTime(self, dest, date, user, n):
        start = time.time()
        result = self.dfs(dest, date, user, n)
        end = time.time()
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

        print("\n=== BFS Results ===")
        for name in bfs_results:
            travel_date = datetime.strptime(str(self.getDate(name)), "%Y%m%d").date()
            print(f"{name} (Travel Date: {travel_date.strftime('%Y-%m-%d')})")
        print(f"BFS Time: {bfs_time:.6f} seconds")

        print("\n=== DFS Results ===")
        for name in dfs_results:
            travel_date = datetime.strptime(str(self.getDate(name)), "%Y%m%d").date()
            print(f"{name} (Travel Date: {travel_date.strftime('%Y-%m-%d')})")
        print(f"DFS Time: {dfs_time:.6f} seconds\n")


    # FUTURE WORK

    def addFriend(self, name, friend) -> bool: #adds a friend to a user
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].addFriend(friend)

    def removeFriend(self, name, friend) -> bool: #removes a friend
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].removeFriend(friend)
