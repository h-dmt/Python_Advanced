from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> str:
        valid_types = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

        if horse_type in valid_types.keys():

            if [h for h in self.horses if h.name == horse_name]:
                raise Exception(f"Horse {horse_name} has been already added!")

            horse = valid_types[horse_type](horse_name, horse_speed)

            if horse:
                self.horses.append(horse)
                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:

        if [j for j in self.jockeys if j.name == jockey_name]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)

        if jockey:
            self.jockeys.append(jockey)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        if [r for r in self.horse_races if r.race_type == race_type]:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)

        if race:
            self.horse_races.append(race)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = next(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, reversed(self.horses)))

        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        else:
            jockey.horse = horse
            jockey.horse.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> str:

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if [j for j in race.jockeys if j.name == jockey_name]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        else:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str) -> str:
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        top_speed = 0
        for horse in self.horses:
            if horse.speed > top_speed and horse.is_taken:
                top_speed = horse.speed
                winner = horse

        jockey = next(filter(lambda j: j.horse.name == winner.name, self.jockeys))

        return f"The winner of the {race_type} race, " \
               f"with a speed of {top_speed}km/h is {jockey.name}! Winner's horse: {winner.name}."
