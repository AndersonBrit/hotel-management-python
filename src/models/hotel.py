# src/models/hotel.py
# Main management class responsible for rooms and reservations

from datetime import datetime
from .reservation import Reservation
from .room_status import RoomStatus

class Hotel:
    def __init__(self, name):
        self.name = name               # Hotel name
        self.rooms = []                # List of Room objects
        self.reservations = []         # List of Reservation objects

    def add_room(self, room):
        """Add a Room object to the hotel."""
        self.rooms.append(room)

    def list_rooms(self):
        """Print all rooms in the hotel with their current status."""
        for room in self.rooms:
            print(room)

    def available_rooms(self):
        """Print only rooms that are currently available."""
        for room in self.rooms:
            if room.status == RoomStatus.AVAILABLE:
                print(room)

    def make_reservation(self, room, start_date, end_date):
        """Attempt to reserve a room for a given date range."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        if end <= start:
            print("Error: End date must be after start date.")
            return False

        # Check for conflicts with existing reservations
        for reservation in self.reservations:
            if reservation.room == room:
                r_start = datetime.strptime(reservation.start_date, "%Y-%m-%d")
                r_end = datetime.strptime(reservation.end_date, "%Y-%m-%d")
                if start < r_end and end > r_start:
                    print("Error: Room already reserved in this period.")
                    return False

        # If no conflicts, create the reservation and mark room as occupied
        reservation = Reservation(room, start_date, end_date)
        self.reservations.append(reservation)
        room.occupy()
        return True

    def list_reservations(self):
        """Print all current reservations."""
        for reservation in self.reservations:
            print(reservation)
