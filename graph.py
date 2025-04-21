class Graph:
    def __init__(self):
        self.users = {} #name ,id
        self.friends = [] #list of friends
        self.destination = [] #list of destinations
        self.date = [] #list of dates

    def getDestination(self, user): #returns destination of user
        return self.users[user].getDestination()

    def getDate(self, user): #returns date of user
        return self.users[user].getDate()

    def insert(self, username, friends, destination, date, id): #insert function for new user
        if username not in self.users: #check if user is already in system
            newUser = User(username, friends, destination, date, id)
            self.users[username] = newUser

    def addFriend(self, name, friend) -> bool: #adds a friend to a user
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].addFriend(friend)


    def removeFriend(self, name, friend) -> bool: #removes a friend
        if name not in self.users or friend not in self.users:
            return False
        return self.users[name].removeFriend(friend)


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

        while q: #loop while there are still users to be searched
            cur = q.pop(0)
            if cur not in visited: #check if you have already visited notde
                visited.add(cur)
                if cur.getDestination() == dest and low <= cur.getDate() <= high: #if destination matches and date is in range add to out
                    out.append(cur)
                for friend in cur.getFriends(): #add friends of cur to the queue
                    if friend not in visited and friend not in out:
                        q.append(friend)
        return out
    
    def dfs(self, dest, date, user) ->list:
        stack=[]
        visited =set()
        out=[]
        start=self.users.get(user)
        if start is None:
            return []
        stack.append(stack)

        while stack:
            cur=stack.pop()
            if cur in visited:
                continue
            visited.add(cur)

            if self.destination[cur]==dest and self.date[cur]==date:
                out.append(cur)

            for friend in self.friends[cur]:
                if friend not in visited:
                    stack.append(friend)
                    

        return out


        