# src/models/quarto.py
# Room entity representing a hotel room

from .room_status import RoomStatus

class Room:
    def __init__(self, number, room_type):
        self.number = number               # Room number
        self.room_type = room_type         # Type of room (e.g., Single, Double, Suite)
        self.status = RoomStatus.AVAILABLE # Initial status is available

    def occupy(self):
        """Mark the room as occupied if it is available."""
        if self.status == RoomStatus.AVAILABLE:
            self.status = RoomStatus.OCCUPIED
            return True
        return False

    def release(self):
        """Mark the room as available if it is currently occupied."""
        if self.status == RoomStatus.OCCUPIED:
            self.status = RoomStatus.AVAILABLE
            return True
        return False

    def __str__(self):
        """Return a readable string representation of the room."""
        return f"Room {self.number} | Type: {self.room_type} | Status: {self.status.value}"
