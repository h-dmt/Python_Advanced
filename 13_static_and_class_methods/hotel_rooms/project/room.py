
class Room:
    def __init__(self, number: int, capacity: int):
        self.guests = 0
        self.is_taken = False
        self.number = number
        self.capacity = capacity

    def take_room(self, people):
        # if the room is not taken, and there is enough space, the guests take the room.
        # Otherwise, the method should return "Room number {number} cannot be taken"

        if people <= self.capacity and not self.is_taken:
            self.is_taken = True
            self.guests = people

        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0

        else:
            return f"Room number {self.number} is not taken"
