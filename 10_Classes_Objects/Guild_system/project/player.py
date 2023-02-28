class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost) -> str:
        # ◦ Adds the skill and the corresponding mana cost to the dictionary of skills.
        # Returns "Skill {skill_name} added to the collection of the player {player_name}"
        # ◦ If the skill is already in the collection, returns "Skill already added"

        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

        else:
            return "Skill already added"

    def player_info(self) -> str:
        """
        Name: {player_name}
        Guild: {guild_name}
        HP: {hp}
        MP: {mp}
        ==={skill_name_1} - {skill_mana_cost}
        ==={skill_name_2} - {skill_mana_cost}
        ==={skill_name_N} - {skill_mana_cost}"
        """
        print_out = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        for skill in self.skills:
            print_out.append(f"==={skill} - {self.skills[skill]}")

        return '\n'.join(print_out)
