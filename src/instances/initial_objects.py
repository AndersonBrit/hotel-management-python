# src/instances/obj.py
# This file creates initial objects for the hotel management system.
# It initializes the hotel, adds rooms, and creates sample reservations.

from models import Hotel, Room

# Create the main Hotel instance
hotel = Hotel("Hotel")  # Hotel object representing our hotel

# Create and add rooms to the hotel
hotel.add_room(Room(101, "Single"))  # Room 101, type: Single
hotel.add_room(Room(102, "Double"))  # Room 102, type: Double
hotel.add_room(Room(103, "Suite"))   # Room 103, type: Suite

# Make a sample reservation using the hotel's method
hotel.make_reservation(
    hotel.rooms[1],          # Room 102 (index 1 in the list)
    "2025-12-25",            # Start date of reservation
    "2025-12-30"             # End date of reservation
)
