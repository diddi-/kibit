from dataclasses import dataclass

from kibit.modules.module_arguments import ModuleArguments


@dataclass
class PingArguments(ModuleArguments):
    destination: str
    count: int = 1
