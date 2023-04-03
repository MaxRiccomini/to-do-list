import datetime

class ToDoList:
    def __init__(self, task, current_date, completion_date, completion_status):
        self.task = task
        self.current_date = current_date
        self.completion_date = completion_date
        self.completion_status = completion_status

        def add_task(self, task):
            tasks = []
            self.task = task
            task = input("Enter Task: ")

