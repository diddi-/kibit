from abc import abstractmethod, ABC

from kibit.modules.module_arguments import ModuleArguments


class Module(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def arguments(self):
        pass

    @abstractmethod
    def run(self, args: ModuleArguments) -> bool:
        pass
