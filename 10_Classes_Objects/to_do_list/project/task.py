class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        # ◦ Changes the name of the task and returns the new name.
        # ◦ If the new name is the same as the current name, returns "Name cannot be the same."
        if self.name != new_name:
            self.name = new_name
            return self.name

        else:
            return "Name cannot be the same."

    def change_due_date(self, new_date: str):
        # ◦ Changes the due date of the task and returns the new date.
        # ◦ If the new date is the same as the current date, returns "Date cannot be the same."
        if new_date != self.due_date:
            self.due_date = new_date
            return self.due_date

        else:
            return "Date cannot be the same."

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        # ◦ The comment number value represents the index of the comment we want to edit.
        # The method should change the comment and return all the comments,
        # separated by comma and space (", ")
        # ◦ If the comment number is out of range, returns "Cannot find comment."
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return f"{', '.join(self.comments)}"

        else:
            return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

