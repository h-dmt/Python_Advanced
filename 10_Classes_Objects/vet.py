
class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        # ◦ If there is space in the vet clinic, adds the animal to both animals' lists and
        # returns a message: "{name} registered in the clinic"
        # ◦ Otherwise, returns "Not enough space"
        if Vet.space > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"

        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        # ◦ If the animal is in the clinic, removes it from both animals' lists and returns
        # "{animal} unregistered successfully"
        # ◦ Otherwise, returns "{animal} not in the clinic"
        if animal_name in Vet.animals and animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"

        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        # • Returns info about the vet, the number of animals in his list and the free space in the clinic:
        # "{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
