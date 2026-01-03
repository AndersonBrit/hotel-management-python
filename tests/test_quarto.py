# tests/test_room.py

# Unit tests for the Room class

import unittest
from models.room import Room
from models.room_status import RoomStatus


class TestRoom(unittest.TestCase):
    """
    Test suite for the Room class.
    Responsible for validating room status transitions.
    """

    def test_occupy_available_room(self):
        """
        Test occupying a room when it is available.
        Expected result:
        - Operation succeeds
        - Room status changes to OCCUPIED
        """
        room = Room(101, "Single")
        result = room.occupy()

        self.assertTrue(result)
        self.assertEqual(room.status, RoomStatus.OCCUPIED)

    def test_occupy_occupied_room(self):
        """
        Test attempting to occupy a room that is already occupied.
        Expected result:
        - Operation fails
        - Room status remains OCCUPIED
        """
        room = Room(101, "Single")
        room.occupy()
        result = room.occupy()

        self.assertFalse(result)

    def test_release_room(self):
        """
        Test freeing an occupied room.
        Expected result:
        - Operation succeeds
        - Room status changes back to AVAILABLE
        """
        room = Room(101, "Single")
        room.occupy()
        result = room.release()

        self.assertTrue(result)
        self.assertEqual(room.status, RoomStatus.AVAILABLE)


if __name__ == "__main__":
    unittest.main()
