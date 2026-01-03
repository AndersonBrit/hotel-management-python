# src/interface/reservations.py
# Functions related to reservation management and display

from instances.initial_objects import *   # Import the hotel object with rooms and reservations
from utils import clear_screen, waiting  # Utility functions for UI
from models.room_status import RoomStatus  # Enum for room status (AVAILABLE, OCCUPIED)


def make_reservation_menu():
    """
    Displays the reservation menu, collects user input for room and dates,
    and attempts to create a reservation.
    """
    clear_screen()  # Clear the terminal
    print("\nMake a reservation:")

    # Display all rooms with their number, type, and status
    for room in hotel.rooms:
        print(f"Room {room.number} ({room.room_type}) - {room.status.value}")

    try:
        # Ask the user for room number and reservation dates
        room_number = int(input("Room number to reserve: "))
        start_date = input("Start date (YYYY-MM-DD): ")
        end_date = input("End date (YYYY-MM-DD): ")

        # Find the room object corresponding to the number entered
        selected_room = next((r for r in hotel.rooms if r.number == room_number), None)

        if selected_room:
            # Attempt to make the reservation using Hotel's method
            success = hotel.make_reservation(selected_room, start_date, end_date)
            if success:
                print(f"Room {room_number} reserved successfully!")
            else:
                print("Unable to make the reservation. Check dates or availability.")
        else:
            print("Room not found.")

    except ValueError:
        # Handle invalid input for room number
        print("Invalid room number.")

    waiting()  # Pause to allow the user to read messages


def list_reservations():
    """
    Displays all current reservations in the hotel.
    """
    clear_screen()
    print("\nCurrent reservations:")

    # Use the Hotel's method to list reservations
    hotel.list_reservations()
    waiting()  # Pause for user
