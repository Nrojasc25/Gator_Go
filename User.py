from datetime import datetime

class user:
    def __init__(self, username, friends, destination, date, id):
        self.username = username
        self.friends = friends
        self.destination = destination
        self.date = datetime.strptime(str(date), "%Y%m%d").date()
        self.id = id

    def getFriends(self) -> list: #returns friends list (ids)
        return self.friends

    def getDestination(self): #returns destination
        return self.destination

    def getDate(self): #returns date of travel
        return self.date
    
    def getID(self):
        return self.id  
    
    def getUsername(self):
        return self.username
    
    
    # FUTURE WORK

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