from dataclasses import dataclass

from kibit.modules.module_arguments import ModuleArguments


@dataclass
class SshArguments(ModuleArguments):
    host: str
