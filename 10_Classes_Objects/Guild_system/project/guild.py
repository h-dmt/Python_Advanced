from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        # ◦ Adds the player to the guild and returns
        # "Welcome player {player_name} to the guild {guild_name}".
        # Remember to change the player's guild in the player class.
        # ◦ If he is already in the guild, returns "Player {player_name} is already in the guild."
        # ◦ If the player is in another guild, returns "Player {player_name} is in another guild."

        if player.guild not in ["Unaffiliated", self.name]:
            return f"Player {player.name} is in another guild."

        elif player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        else:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str) -> str:
        # ◦ Removes the player from the guild and returns
        # "Player {player_name} has been removed from the guild.".
        # Remember to change the player's guild in the player class to "Unaffiliated".
        # ◦ If there is no such player in the guild, returns "Player {player_name} is not in the guild."

        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                p.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        # Returns the guild's information, including the players in the guild, in the format:
        """
        Guild: {guild_name}
        {first_player's info}
        …
        {Nplayer's info}
        """
        print_out = [f"Guild: {self.name}"]

        for player in self.players:
            print_out.append(f"{player.player_info()}")

        return '\n'.join(print_out)
