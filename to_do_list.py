class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def task_done(self, task):
        task.completed = True

    def show_tasks(self):
        for task in self.tasks:
            print(task)


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.description}"


todo_list = Todolist()


