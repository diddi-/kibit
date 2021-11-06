from __future__ import annotations

from typing import Type

from kibit.modules.module import Module
from kibit.modules.module_arguments import ModuleArguments


class Task:
    def __init__(self, task_id: int, name: str, module: Type[Module], arguments: ModuleArguments):
        self.task_id = task_id
        self.name = name
        self.module = module
        self.arguments = arguments
        self.trace = False
