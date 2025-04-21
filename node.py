class UserNode:
    def __init__(self, name, destination=None, date=None):
        self.name = name
        self.destination = destination
        self.date = date
        self.friends = set()  # Using a set to avoid duplicates

    def add_friend(self, other_node):
        self.friends.add(other_node)

    def remove_friend(self, other_node):
        self.friends.discard(other_node)

    def __repr__(self):
        return f"UserNode({self.name})"
