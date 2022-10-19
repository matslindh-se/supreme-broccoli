class UserService:
    def __init__(self):
        self.users = set()

    def add_user(self, username):
        self.users.add(username)

    def remove_user(self, username):
        if self.has_user(username):
            self.users.remove(username)

    def has_user(self, username):
        return username in self.users        
