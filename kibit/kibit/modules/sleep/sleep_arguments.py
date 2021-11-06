from dataclasses import dataclass

from kibit.modules.module_arguments import ModuleArguments


@dataclass
class SleepArguments(ModuleArguments):
    min_sec: int = 0
    max_sec: int = 0
