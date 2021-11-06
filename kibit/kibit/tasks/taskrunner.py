import multiprocessing

from kibit.tasks.progress import Progress
from kibit.spec.spec import Spec
from kibit.tasks.worker import Worker


class TaskRunner:
    def __init__(self, spec: Spec):
        self.spec = spec

    def start(self):
        task_queue = multiprocessing.Queue()
        result_queue = multiprocessing.Queue()
        progress = Progress()
        workers = []
        for task in self.spec.tasks:
            task_queue.put(task)
            progress.add_task(task)

        for i in range(self.spec.settings.workers):
            w = Worker(task_queue, result_queue)
            w.start()
            workers.append(w)

        results = []
        while len(results) < len(self.spec.tasks):
            result = result_queue.get()
            progress.update(result)
            results.append(result)

        for w in workers:
            w.join()
