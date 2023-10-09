# Import the User, Game, and Card classes from their respective modules
from user import User
from game import Game
from card import Card
import sys

# Define the main function
def main():
    # Initialize empty lists to store users and games
    users = []

    # Define a function for creating a new user
    def create_user():
        username = input("Enter username: ")
        is_admin = input("Is admin? (yes/no): ").lower() == "yes"
        user = User(username, is_admin)
        users.append(user)
        print(f"User '{user.username}' created.")

    # Define a function for creating a game (for normal users)
    def create_game():
        username = input("Enter your username: ")
        user = next((u for u in users if u.username == username), None)
        if user is None:
            print("User not found.")
        elif user.is_admin:
            print("Admin users cannot create games.")
        else:
            game = Game()
            num_cards = int(input("Enter the number of cards to add to the game: "))
            for _ in range(num_cards):
                card = Card()
                game.add_card(card)
            user.create_game(game)
            print(f"Game created by '{user.username}'.")

    # Define a function for showing game history
    def show_game_history():
        username = input("Enter username to show game history: ")
        user = next((u for u in users if u.username == username), None)
        if user is None:
            print("User not found.")
        else:
            print(f"\nGame History for {user.username}:\n")
            for i, game in enumerate(user.games, start=1):
                print(f"Game {i} - Number of Cards: {len(game.cards)}")
                for j, card in enumerate(game.cards, start=1):
                    print(f"  Card {j} - {card}")
                    #print(f"    Numbers Selected: {', '.join(map(str, card.numbers))}")

    # Define a function to list users
    def list_users():
        user_list = User.list_users(users)
        if user_list:
            print("\nList of Created Users:")
            for username in user_list:
                print(username)
        else:
            print("No users created yet.")

    # Define a function to exit the program
    def exit_program():
        print("Exiting the program.")
        sys.exit(0)


    # Define a dictionary to map menu options to functions
    menu_options = {
        "1": create_user,
        "2": create_game,
        "3": show_game_history,
        "4": list_users,
        "5": exit_program, 
    }

    # Main program loop
    while True:
        # Display menu options to the user
        print("\n1. Create User")
        print("2. Create Game (Normal User)")
        print("3. Show Game History")
        print("4. List Users")
        print("5. Exit")

        # Prompt the user for their choice
        choice = input("Enter your choice: ")

        # Check if the choice is a valid menu option
        if choice in menu_options:
            # Call the corresponding function based on the user's choice
            menu_options[choice]()
        else:
            print("Invalid choice. Please select a valid option.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()
