from datetime import timedelta


class TaskResult:
    def __init__(self, task_id, task_name, time_taken: timedelta, success: bool):
        self.task_id = task_id
        self.task_name = task_name
        self.time_taken = time_taken
        self.success = success

    def __str__(self):
        return f"Result of {self.task_name}: {self.success} ({self.time_taken} secs)"
