# tests/test_hotel.py

# Unit tests for the Hotel class

import unittest
from models.hotel import Hotel
from models.room import Room
from models.room_status import RoomStatus


class TestHotel(unittest.TestCase):
    """
    Test suite for the Hotel class.
    Responsible for validating hotel reservations behaviour.
    """

    def test_make_reservation_available_room(self):
        """
        Test making a reservation when the room is available.
        Expected result:
        - Reservation is successful
        - Room status changes to OCCUPIED
        - One reservation is added to the hotel
        """
        hotel = Hotel("Test Hotel")
        room = Room(101, "Single")
        hotel.add_room(room)

        success = hotel.make_reservation(room, "2025-01-01", "2025-01-05")

        self.assertTrue(success)
        self.assertEqual(room.status, RoomStatus.OCCUPIED)
        self.assertEqual(len(hotel.reservations), 1)

    def test_make_reservation_occupied_room(self):
        """
        Test attempting to reserve a room that is already occupied.
        Expected result:
        - Reservation fails
        - No new reservations are added
        """
        hotel = Hotel("Test Hotel")
        room = Room(101, "Single")
        hotel.add_room(room)

        # First reservation (valid)
        hotel.make_reservation(room, "2025-01-01", "2025-01-05")

        # Second reservation attempt (should fail)
        success = hotel.make_reservation(room, "2025-01-10", "2025-01-15")

        self.assertFalse(success)
        self.assertEqual(len(hotel.reservations), 1)


if __name__ == "__main__":
    unittest.main()
