from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.customers = []  # empty list of Customer objects
        self.dvds = []  # empty list of DVD objects
        self.name = name

    @staticmethod
    def dvd_capacity():
        #  returns 15 - the DVD capacity of a movie world

        return 15

    @staticmethod
    def customer_capacity():
        # returns 10 - the customer capacity of a movie world

        return 10

    def add_customer(self, customer: Customer):
        # add the customer if capacity not exceeded
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        # add the DVD if capacity not exceeded
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        # ◦ If the customer has already rented that DVD return
        #       "{customer_name} has already rented {dvd_name}"
        # ◦ If the DVD is rented by someone else, return "DVD is already rented"
        # ◦ If the customer is not allowed to rent the DVD, return
        #       "{customer_name} should be at least {dvd_age_restriction} to rent this movie"
        # ◦ Otherwise, the rent is successful (the DVD is rented and added to the customer's DVDs).
        # Return "{customer_name} has successfully rented {dvd_name}"

        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd not in customer.rented_dvds:

            if not dvd.is_rented:

                if customer.age >= dvd.age_restriction:
                    dvd.is_rented = True
                    customer.rented_dvds.append(dvd)
                    return f"{customer.name} has successfully rented {dvd.name}"

                else:
                    return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

            else:
                return f"DVD is already rented"

        else:
            return f"{customer.name} has already rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        # if the DVD is in the customer, he/she should return it and the method should return the message
        # "{customer_name} has successfully returned {dvd_name}".
        # Otherwise, return "{customer_name} does not have that DVD"

        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        # return the string representation of each customer and each DVD on separate lines

        result = []
        for customer in self.customers:
            result.append(customer.__repr__())

        for dvd in self.dvds:
            result.append(dvd.__repr__())

        return '\n'.join(result)
