class Database:
    """Simulates a basic user database"""
    def __init__(self):
        self.data = {} #simulating a in-memory database

    def add_user(self, user_id, name):
        if user_id in self.data:
            return "User already exists."
        self.data[user_id] = name
        return True

    def get_user(self, user_id):
        return self.data.get(user_id, None)
    
    def remove_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]
            return True
        return "User not found."