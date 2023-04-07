from project.booths.booth import Booth


class OpenBooth(Booth):

    @property
    def get_price_per_person(self):
        return 2.5

    def reserve(self, number_of_people: int) -> None:
        self.price_for_reservation = number_of_people * self.get_price_per_person
        self.is_reserved = True

