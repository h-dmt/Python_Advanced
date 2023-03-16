from abc import ABC, abstractmethod

from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam, ABC):
    def __init__(self, budget: int):
        super().__init__(budget)
        self.budget = budget

    @property
    def sponsor(self):
        return {
            'Petronas': {1: 1_000_000, 3: 500_000},
            'TeamViewer': {5: 100_000, 7: 50_000}
        }

    @property
    def expenses(self):
        return 200_000
