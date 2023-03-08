class Animal:
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self):
        # returns string representation of the animal in the format:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

