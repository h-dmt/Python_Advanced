from project.animal import Animal


class Lion(Animal):
    MONEY = 50

    def __init__(self, name: str, gender: str, age: int, money_for_care=MONEY):
        super().__init__(name, gender, age, money_for_care)
