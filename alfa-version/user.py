class User:
    def __init__(self, username, is_admin=False):
        self.username = username
        self.is_admin = is_admin
        self.games = []  # Store user's games

    def create_game(self, game):
        self.games.append(game)

    def __str__(self):
        return f"Username: {self.username}, Admin: {self.is_admin}"

    def show_numbers_selected(self):
        if not self.games:
            return "No games created by this user."
        result = f"Numbers selected by {self.username}:\n"
        for game in self.games:
            result += f"Game: {game}\n"
        return result

    # Method to list all created users
    @classmethod
    def list_users(cls, users):
        user_list = []
        for user in users:
            user_list.append(user.username)
        return user_list