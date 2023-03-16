from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: RedBullTeam or None = None
        self.mercedes_team: MercedesTeam or None = None

    def register_team_for_season(self, team_name: str, budget: int):
        # • Valid team names: "Red Bull", "Mercedes"
        # • If a team name is valid, register the team with the corresponding name and return the following message:
        #     "{ team name } has joined the new F1 season."
        # • If a team name is invalid, raise ValueError with the message: "Invalid team name!"

        if team_name not in ['Mercedes', 'Red Bull']:
            raise ValueError("Invalid team name!")

        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)

        else:
            self.red_bull_team = RedBullTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        # • If Red Bull or Mercedes haven't registered yet, raise an Exception with the following message:
        #   "Not all teams have registered for the season."
        # • Otherwise, find which team has the better position in the race, calculate every team's revenue,
        # update their budget, and return the following message:
        #   "Red Bull: { Red Bull revenue message }. Mercedes: { Mercedes revenue message }.
        #   { team with better position } is ahead at the { race name } race."

        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        redbull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        team_ahead = None
        if redbull_revenue > mercedes_revenue:
            team_ahead = "Red Bull"
        else:
            team_ahead = "Mercedes"

        return f"Red Bull: {redbull_revenue}. Mercedes: {mercedes_revenue}. " \
               f"{team_ahead} is ahead at the {race_name} race."
