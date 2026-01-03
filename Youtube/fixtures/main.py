class userManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            return "User already exists."
        self.users[username] = email
        return True

    def remove_user(self, username):
        if username not in self.users:
            return "User not found."
        del self.users[username]
        return "User removed successfully."

    def get_user_email(self, username):
        return self.users.get(username, "User not found.")