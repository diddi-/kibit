from importlib_metadata import entry_points

from kibit.modules.module import Module


class ModuleLoader:
    @staticmethod
    def load(name) -> Module:
        discovered_modules = entry_points(group="kibit.modules")
        for m in discovered_modules:
            module = m.load()
            if module.name == name:
                return module
        raise ValueError(f"No such module '{name}'")
