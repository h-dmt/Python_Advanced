from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @property
    @abstractmethod
    def sponsor(self):
        ...

    @property
    @abstractmethod
    def expenses(self):
        ...

    def calculate_revenue_after_race(self, race_pos: int):
        #     • Each team should be able to calculate their revenue
        #     • Each team has its unique sponsors
        #         ◦ Sponsors give the team money if they finish in a certain position or better
        #     • Each team has a different amount of expenses
        revenue = 0

        for prizes in self.sponsor.values():
            for pos in prizes:
                if race_pos <= pos:
                    revenue += prizes[pos]
                    break

        revenue -= self.expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
