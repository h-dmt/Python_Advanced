from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: [Lion, Tiger, Cheetah], price) -> str:
        # • If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah)
        #   to the animals' list, reduce the budget, and return
        #   "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
        # • If you have the capacity, but no budget, return "Not enough budget"
        # • In any other case, you do not have space, and you should return "Not enough space for animal"

        if price <= self.__budget and self.__animal_capacity > 0:

            self.__animal_capacity -= 1
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        if self.__animal_capacity > 0 and price > self.__budget:
            return "Not enough budget"

        elif self.__animal_capacity == 0:
            return "Not enough space for animal"

    def hire_worker(self, worker: [Keeper, Caretaker, Vet]) -> str:
        # • If you have not exceeded the capacity of workers in the zoo for the worker
        #   (instance of Keeper/Caretaker/Vet), add him to the workers and return
        #   "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
        # • Otherwise, return "Not enough space for worker"

        if self.__workers_capacity > 0:

            #self.__workers_capacity -= 1
            self.workers.append(worker)

            return f"{worker.name} the {type(worker).__name__} hired successfully"

        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        # • If there is a worker with that name in the workers' list, remove him and return
        #   "{worker_name} fired successfully"
        # • Otherwise, return "There is no {worker_name} in the zoo"

        try:
            employee = next(filter(lambda n: n.name == worker_name, self.workers))

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        if employee:
            self.workers.remove(employee)
            self.__workers_capacity += 1
            return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        # • If you have enough budget to pay the workers (sum their salaries) pay them and return
        #   "You payed your workers. They are happy. Budget left: {left_budget}"
        # • Otherwise, return "You have no budget to pay your workers. They are unhappy"

        salary_sum = 0
        for employee in self.workers:
            salary_sum += employee.salary

        if salary_sum <= self.__budget:

            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        else:

            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        # • If you have enough budget to take care of the animals, reduce the budget and return
        #   "You tended all the animals. They are happy. Budget left: {left_budget}"
        #   • Otherwise, return "You have no budget to tend the animals. They are unhappy."

        cash_needed = 0
        for animal in self.animals:
            cash_needed += animal.money_for_care

        if cash_needed <= self.__budget:

            self.__budget -= cash_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        else:

            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        # • Increase the budget with the given amount of profit

        self.__budget += amount

    def animals_status(self):
        """
        "You have {total_animals_count} animals
        ----- {amount_of_lions} Lions:
        {lion1}
        …
        {lionN}
        ----- {amount_of_tigers} Tigers:
        {tiger1}
        …
        {tigerN}
        ----- {amount_of_cheetahs} Cheetahs:
        {cheetah1}
        …
        {cheetahN}"
        """
        count = len(self.animals)
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]

        print_out = [f"You have {count} animals", f"----- {len(lions)} Lions:"]
        for lion in lions:
            print_out.append(lion.__repr__())

        print_out.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            print_out.append(tiger.__repr__())

        print_out.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            print_out.append(cheetah.__repr__())

        return '\n'.join(print_out)

    def workers_status(self):
        """
        "You have {total_workers_count} workers
        ----- {amount_of_keepers} Keepers:
        {keeper1}
        …
        {keeperN}
        ----- {amount_of_caretakers} Caretakers:
        {caretaker1}
        …
        {caretakerN}
        ----- {amount_of_vetes} Vets:
        {vet1}
        …
        {vetN}"
        """
        count = len(self.workers)
        keepers = [worker for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker for worker in self.workers if isinstance(worker, Vet)]
        print_out = [f"You have {count} workers", f"----- {len(keepers)} Keepers:"]

        for keeper in keepers:
            print_out.append(keeper.__repr__())

        print_out.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            print_out.append(caretaker.__repr__())

        print_out.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            print_out.append(vet.__repr__())

        return '\n'.join(print_out)
