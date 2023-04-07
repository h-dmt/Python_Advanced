from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int) -> str:

        VALID_MUSICIANS = {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer}

        if musician_type not in VALID_MUSICIANS.keys():
            raise ValueError("Invalid musician type!")
        musician_with_name = [musician for musician in self.musicians if musician.name == name]

        if musician_with_name:
            raise Exception(f"{name} is already a musician!")

        new_musician = VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        names = [band.name for band in self.bands]
        if name in names:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:

        concert = [c for c in self.concerts if c.place == place]

        if concert:
            concert = concert[0]
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        # If there isn't a band with the given name, raise an Exception
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        # If there isn't a musician with the given name who is a member of the given band, raise an Exception
        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        # If there is NOT at least one member of each type
        # (at least 1 singer, at least 1 drummer, and at least 1 guitarist), raise an Exception
        band = next(filter(lambda b: b.name == band_name, self.bands))
        for type_musician in ("Guitarist", "Drummer", "Singer"):
            try:
                next(filter(lambda b: b.__class__.__name__ == type_musician, band.members))
            except StopIteration:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        ROCK_SKILLS = {"Drummer": ["play the drums with drumsticks"],
                       "Singer": ["sing high pitch notes"],
                       "Guitarist": ["play rock"]}

        METAL_SKILLS = {"Drummer": ["play the drums with drumsticks"],
                        "Singer": ["sing low pitch notes"],
                        "Guitarist": ["play metal"]}

        JAZZ_SKILLS = {"Drummer": ["play the drums with drum brushes"],
                       "Singer": ["sing high pitch notes", "sing low pitch notes"],
                       "Guitarist": ["play jazz"]}

        genre_skills = {"Jazz": JAZZ_SKILLS, "Metal": METAL_SKILLS, "Rock": ROCK_SKILLS}
        # find concert
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        # select needed skills according to type of concert
        SKILLS = genre_skills[concert.genre]

        # check all musicians have the required skills
        for musician in band.members:
            for required_skill in SKILLS[musician.__class__.__name__]:
                if required_skill not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
