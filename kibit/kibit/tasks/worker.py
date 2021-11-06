from datetime import datetime
from multiprocessing import Process, Queue

import typing
from queue import Empty

from kibit.tasks.task import Task
from kibit.tasks.task_result import TaskResult


class Worker(Process):
    def __init__(self, task_queue: Queue, result_queue: Queue):
        super().__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue

    def execute_task(self, task: Task):
        start = datetime.now()
        try:
            result = task.module().run(task.arguments)
            self.result_queue.put(
                TaskResult(task.task_id, task.name, datetime.now() - start, result))
        except Exception as e:
            self.result_queue.put(
                TaskResult(task.task_id, task.name, datetime.now() - start, False))
            if task.trace:
                raise e

    def run(self):
        try:
            while task := typing.cast(Task, self.task_queue.get_nowait()):
                self.execute_task(task)
        except Empty:
            pass
