from project.person import Person


class Child(Person):
    # Pass is sufficient in this case ...
    def __init__(self, name, age):
        super().__init__(name, age)
