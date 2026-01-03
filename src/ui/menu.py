# src/interface/menu.py
# Functions related to displaying the main menu and getting user input

from utils import clear_screen

def menu():
    """
    Clears the terminal screen, displays the main hotel menu,
    and returns the option selected by the user.
    """
    clear_screen()  # Clear the screen for a clean menu display

    # Print menu options
    print("\n=== Hotel Menu ===")
    print("1. List all rooms")
    print("2. Show available rooms")
    print("3. Make a reservation")
    print("4. List reservations")
    print("0. Exit")
    print("")

    # Get user input
    option = input("Choose an option: ")
    return option
