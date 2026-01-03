# src/main.py
# Entry point of the application.
# This file runs the main program loop,
# displays menus, and coordinates the use of classes and objects.

from instances.initial_objects import *                   # Imports initial objects (hotel, rooms, reservations)
from utils import clear_screen, waiting                   # Utility functions
from ui.menu import menu                                  # Menu function
from ui.rooms import list_rooms, list_available_rooms
from ui.reservations import make_reservation_menu, list_reservations

# Main application loop
while True:
    choice = menu()  # Display menu and get user choice

    if choice == "1":
        list_rooms()            # List all rooms
    elif choice == "2":
        list_available_rooms()  # Show available rooms
    elif choice == "3":
        make_reservation_menu() # Make a reservation
    elif choice == "4":
        list_reservations()     # List all reservations
    elif choice == "0":
        clear_screen()
        print("Program terminated")
        break
    else:
        clear_screen()
        print("Invalid option. Please try again.")
        waiting()
