from project.task import Task


class Section:
    def __init__(self, name: str):
        self.tasks = []
        self.name = name

    def add_task(self, new_task: Task):
        # ◦ Adds a new task to the collection and returns "Task {task details} is added to the section"
        # ◦ If the task is already in the collection,
        # returns "Task is already in the section {section_name}"
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        # ◦ Changes the task to completed (True) and returns "Completed task {task_name}"
        # ◦ If the task is not found, returns "Could not find task with the name {task_name}"
        try:
            found_task = next(filter(lambda s: s.name == task_name, self.tasks))
            found_task.completed = True
            return f"Completed task {task_name}"

        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        # Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
        counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                counter += 1

        return f"Cleared {counter} tasks."

    def view_section(self):
        # Returns information about the section and its tasks.
        return_output = [f"Section {self.name}:"]
        for task in self.tasks:
            return_output.append(task.details())

        return '\n'.join(return_output)
