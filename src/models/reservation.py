# src/models/reserva.py
# Represents a reservation linking a room to a date range

class Reservation:
    def __init__(self, room, start_date, end_date):
        self.room = room                   # Room object being reserved
        self.start_date = start_date       # Reservation start date (YYYY-MM-DD)
        self.end_date = end_date           # Reservation end date (YYYY-MM-DD)

    def __str__(self):
        """Return a readable string representation of the reservation."""
        return f"Room {self.room.number} | {self.start_date} → {self.end_date}"
