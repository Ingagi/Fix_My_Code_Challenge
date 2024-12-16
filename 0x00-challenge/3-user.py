class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_password(self, password):
        return self.password == password

# Example usage:
user = User("Test User", "password123")
print(user.is_valid_password("password123"))  # Should print True

