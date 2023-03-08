from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player) -> str:
        # • If the player is already in the team, return "Player {name} has already joined"
        # • Otherwise, add the player to the team and return "Player {name} joined team {team_name}"

        if player in self.__players:
            return f"Player {player.name} has already joined"

        else:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> [str, None]:
        # • Remove the player and return him
        # • If the player is not in the team, return "Player {player_name} not found"
        try:
            player = next(filter(lambda n: n.name == player_name, self.__players))

        except StopIteration:
            return f"Player {player_name} not found"

        if player:
            self.__players.remove(player)
            return player
