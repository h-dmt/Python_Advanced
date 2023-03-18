from abc import ABC, abstractmethod
#import time


class Work(ABC):

    @abstractmethod
    def work(self):
        pass


class Eat(ABC):

    @abstractmethod
    def eat(self):
        pass


class Worker(Work, Eat):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        #time.sleep(5)


class SuperWorker(Work):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        #time.sleep(3)


class Manager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class ManagerWork(Manager):

    def set_worker(self, worker):

        assert isinstance(worker, Work), "`worker` must be of type {}".format(Work)

        self.worker = worker

    def manage(self):
        self.worker.work()


class ManagerBreak(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Eat), "`worker` must be of type {}".format(Eat)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(Work):

    def work(self):
        print("I'm a robot. I'm working....")


work_manager = ManagerWork()
work_manager.set_worker(Worker())
break_manager = ManagerBreak()
break_manager.set_worker(Worker())
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()

except:
    pass
