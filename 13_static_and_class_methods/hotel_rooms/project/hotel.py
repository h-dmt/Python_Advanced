from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        # creates a new instance with name "{stars_count} stars Hotel"
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = room.take_room(people)

        if not result:
            self.guests += people

        else:
            return result

    def free_room(self, room_number):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        people = room.guests
        res_output = room.free_room()

        if not res_output:
            self.guests -= people

        else:
            return res_output

    def status(self):
        free_rooms = [str(free_room.number) for free_room in self.rooms if not free_room.is_taken]
        taken_rooms = [str(taken_room.number) for taken_room in self.rooms if taken_room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
