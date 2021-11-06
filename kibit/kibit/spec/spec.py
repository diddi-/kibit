from __future__ import annotations

from typing import List

from kibit.modules.module_loader import ModuleLoader
from kibit.spec.spec_settings import SpecSettings
from kibit.tasks.task import Task


class Spec:
    def __init__(self):
        self.settings = SpecSettings()
        self.tasks: List[Task] = []

    @staticmethod
    def load(data: dict) -> Spec:
        s = Spec()
        if "settings" in data.keys():
            s.settings = SpecSettings.load(data.get("settings"))

        t_id = 0
        for t in data.get("tasks"):
            task_name = t.pop("name")
            trace = None
            if "trace" in t.keys():
                trace = t.pop("trace")
            if len(t.keys()) > 1:
                raise ValueError("Only one module can be specified per task")
            if len(t.keys()) == 0:
                raise ValueError(f"No module specified for task '{task_name}'")
            module_name = list(t.keys()).pop()
            module = ModuleLoader.load(module_name)
            arguments = module.arguments(**t[module_name])
            task = Task(t_id, task_name, module, arguments)
            if trace is not None:
                task.trace = trace
            s.tasks.append(task)
            t_id += 1
        return s
