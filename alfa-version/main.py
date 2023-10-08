from user import User
from game import Game
from card import Card

def main():
    users = []
    games = []

    while True:
        print("\n1. Create User")
        print("2. Create Game (Normal User)")
        print("3. Show Game History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            is_admin = input("Is admin? (yes/no): ").lower() == "yes"
            user = User(username, is_admin)
            users.append(user)
            print(f"User '{user.username}' created.")

        elif choice == "2":
            username = input("Enter your username: ")
            user = next((u for u in users if u.username == username), None)
            if user is None:
                print("User not found.")
            elif user.is_admin:
                print("Admin users cannot create games.")
            else:
                game = Game()
                card = Card()
                game.add_card(card)
                games.append((user, game))
                print(f"Game created by '{user.username}'.")

        elif choice == "3":
            print("\nGame History:")
            for user, game in games:
                print(f"User: {user.username}, Game: {game}")

        elif choice == "4":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
