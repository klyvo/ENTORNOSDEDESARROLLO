class User:
    def __init__(self, id, username, password, email, idrole, token=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"