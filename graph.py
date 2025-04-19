class Graph:
    def __init__(self):
        self.users = {} #name ,id
        self.friends = [] #list of friends
        self.destination = [] #list of destinations
        self.date = [] #list of dates

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
