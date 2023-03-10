class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def edit(self, new_name: str):
        # edit the name of the category
        self.name = new_name

    def __repr__(self):
        # returns a string representation of the category in the following format: "Category {id}: {name}"

        return f"Category {self.id}: {self.name}"
