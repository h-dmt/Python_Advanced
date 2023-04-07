from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    Valid_delicacies = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    Valid_booths = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth, }

    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        # • If a delicacy with that name exists, raise an Exception with the following message:
        # "{delicacy name} already exists!"
        # • If the delicacy type is not valid, raise an Exception with the following message:
        # "{type of delicacy} is not on our delicacy menu!"
        # • Otherwise, create the delicacy, add it to the delicacies' list, and return the following message:
        # "Added delicacy {delicacy name} - {type of delicacy} to the pastry shop."
        # • Valid types of delicacies are: "Gingerbread" and "Stolen"

        delicacy = [d for d in self.delicacies if d.name == name]

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.Valid_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.Valid_delicacies[type_delicacy](name, price)  # creates an instance of the delicacy
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        # The method creates a booth of the given type and adds it to the booths' collection.
        # All booth numbers should be unique.
        #    • If a booth with that number exists, raise an Exception with the following message:
        #       "Booth number {booth number} already exists!"
        #    • If the booth type is not valid, raise an Exception with the following message:
        #       "{type of booth} is not a valid booth!"
        #    • Otherwise, create the booth, add it to the booths' list and return the following message:
        #       "Added booth number {booth number} in the pastry shop."
        #    • Valid types of delicacies are: "Open Booth" and "Private Booth"

        booth = [b for b in self.booths if b.booth_number == booth_number]

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.Valid_booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.Valid_booths[type_booth](booth_number, capacity)  # creates an instance of the booth
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        # Finds the first booth that is not reserved and whose capacity is enough for the number of people
        # provided.
        # • If there is no such booth, raise an Exception with the following message:
        #     "No available booth for {number of people} people!"
        # • Otherwise, reserves the booth and return:
        #     "Booth {booth number} has been reserved for {number of people} people."

        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and not b.is_reserved, self.booths))

        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        # Finds the booth with the provided number and the delicacy with the provided name;
        # and orders the delicacy for that booth.
        # • If there is no such booth, raise an Exception with the following message:
        #   "Could not find booth {booth number}!"
        # • If there is no such delicacy, raise an Exception with the following message:
        #   "No {delicacy name} in the pastry shop!"
        # • Otherwise, order the delicacy for that booth and return:
        #   "Booth {booth number} ordered {delicacy name}."

        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        except StopIteration:
            raise Exception("Could not find booth {booth number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))

        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int) -> str:
        # • Finds the booth with the same booth's number (the booth's number will always be valid).
        # • Calculates the bill for that booth taking the price for reservation and all the price of
        #   all orders. The bill is added to the pastry shop's total income.
        # • Removes all the ordered delicacies, frees the booth, and sets the price for reservation to 0.
        # • Finally returns:
        #   "Booth {booth number}:"
        #   "Bill: {bill - formatted to the second decimal}lv."

        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        self.income += bill

        return f"Booth {booth_number}:\n"\
               f"Bill: {bill:.2f}lv."

    def get_income(self) -> str:
        # • Returns the total income for the pastry shop for all completed bills in the format:
        #   "Income: {income - formatted to the second decimal place}lv."

        return f"Income: {self.income:.2f}lv."

