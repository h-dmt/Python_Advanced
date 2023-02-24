from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            out_string = pokemon.pokemon_details()
            return f"Caught {out_string}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for pokemon_in_list in self.pokemons:
            pokemon_in_list: Pokemon
            if pokemon_in_list.name == pokemon_name:
                self.pokemons.remove(pokemon_in_list)
                return f"You have released {pokemon_name}"

        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        data_return = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for pokemon_name in self.pokemons:
            pokemon_name: Pokemon
            data_return.append(f"- {pokemon_name.pokemon_details()}")
        return '\n'.join(data_return)


"""pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
"""
