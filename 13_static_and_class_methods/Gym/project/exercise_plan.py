class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

        ExercisePlan.id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        # creates new instance using the provided information

        hours *= 60  # convert to minutes!!!
        return cls(trainer_id, equipment_id, hours)

    @staticmethod
    def get_next_id():
        # static method that returns the id that will be given to the next plan
        return ExercisePlan.id

    def __repr__(self):
        # returns the information about the plan in the following format:
        # "Plan <{id}> with duration {duration} minutes"

        return f"Plan <{self.id}> with duration {self.duration} minutes"
