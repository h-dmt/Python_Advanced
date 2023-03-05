class Mammal:
    _Mammal__kingdom = "animals"

    def __init__(self, name, mammal_type, sound):
        self.name = name
        self.sound = sound
        self.type = mammal_type

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self._Mammal__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
