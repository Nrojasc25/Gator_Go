from datetime import datetime

class user:
    def __init__(self, username, friends, destination, date, id):
        self.username = username
        self.friends = friends
        self.destination = destination
        self.date = datetime.strptime(str(date), "%Y%m%d").date()
        self.id = id

    def getFriends(self, user) -> list: #returns friends list
        return self.friends

    def getDestination(self, user): #returns destination
        return self.destination

    def getDate(self, user): #returns date of travel
        return self.date

    def getID(self, user):  #returns user ID
        return self.id

    def addFriend(self, friend) -> bool: #adds friend into friend list
        if friend not in self.friends:
            self.friends.append(friend)
            return True
        return False

    def removeFriend(self, friend) -> bool: #removes friend from friends list
        if friend not in self.friends:
            return False
        self.friends.remove(friend)
        return True