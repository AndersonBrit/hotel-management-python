# src/models/estado_quarto.py
# Defines the possible states of a hotel room

from enum import Enum

class RoomStatus(Enum):
    AVAILABLE = "available"   # Room is free and can be reserved
    OCCUPIED = "occupied"     # Room is currently occupied
