class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):

    def test_worker_initialization(self):
        worker = Worker("Mario", 2000, 88)
        name = worker.name
        salary = worker.salary
        energy = worker.energy
        self.assertEqual(name, "Mario")
        self.assertEqual(salary, 2000)
        self.assertEqual(energy, 88)

    def test_rest_method(self):
        worker = Worker("Mario", 2000, 88)
        worker.rest()
        energy = worker.energy
        self.assertEqual(energy, 89)

    def test_no_energy(self):
        worker = Worker("Mario", 2000, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_money_salary(self):
        worker = Worker("Mario", 2000, 88)
        worker.work()
        money = worker.money
        self.assertEqual(money, 2000)

    def test_energy_decrease(self):
        worker = Worker("Mario", 2000, 88)
        worker.work()
        energy = worker.energy
        self.assertEqual(energy, 87)

    def test_get_info(self):
        worker = Worker("Mario", 2000, 88)
        worker.work()
        text = worker.get_info()
        self.assertEqual(text, "Mario has saved 2000 money.")


if __name__ == '__main__':
    unittest.main()
