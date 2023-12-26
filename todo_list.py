class ToDoList:
    def __init__(self, to_do_list_id, tasks, owner_id):
        self.to_do_list_id = to_do_list_id
        self.tasks = tasks
        self.owner_id = owner_id

    def createTask(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def updateTask(self, task_index, new_task):
        if task_index < len(self.tasks):
            self.tasks[task_index] = new_task
            print("Task updated:", new_task)
        else:
            print("Invalid task index")

    def viewTasks(self):
        print("Tasks:", self.tasks)
        return self.tasks
