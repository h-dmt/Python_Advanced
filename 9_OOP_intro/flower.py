# A class called Flower. Upon initialization, the class should receive a name (string) and
# a water_requirements (number). The flower should also have an instance attribute called is_happy
# (False by default). Add two additional methods to the class:
#     • water(quantity) - it will water the flower. Each time check if the quantity is greater than or
#     equal to the required. If it is - the flower becomes happy (set is_happy to True).
#     • status() - it should return "{name} is happy" if the flower is happy, otherwise it should return
#     "{name} is not happy".

class Flower:
    def __init__(self, name, water_requirements, is_happy=False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy
        self.state = 'not happy'

    def water(self, qty):
        if qty >= self.water_requirements:
            self.is_happy = True
            self.state = 'happy'
        else:
            self.is_happy = False
            self.state = 'not happy'

    def status(self):
        return f"{self.name} is {self.state}"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())