# src/interface/rooms.py
# Functions related to room listing and availability display

from instances.initial_objects import *   # Import hotel object
from utils import clear_screen, waiting  # Utility functions for UI
from models.room_status import RoomStatus  # Enum for room status


def list_rooms():
    """
    Displays all rooms in the hotel with their number, type, and current status.
    """
    clear_screen()
    print("\nAll rooms:")

    for room in hotel.rooms:
        print(f"Room {room.number} ({room.room_type}) - {room.status.value}")

    waiting()  # Pause for user


def list_available_rooms():
    """
    Displays only rooms that are currently available for reservation.
    """
    clear_screen()
    print("\nAvailable rooms:")

    for room in hotel.rooms:
        if room.status == RoomStatus.AVAILABLE:
            print(f"Room {room.number} ({room.room_type})")

    waiting()  # Pause for user
