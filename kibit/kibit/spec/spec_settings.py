from __future__ import annotations

class SpecSettings:
    def __init__(self, workers: int = 5):
        self.workers = workers

    @staticmethod
    def load(data: dict) -> SpecSettings:
        s = SpecSettings()
        if "workers" in data.keys():
            s.workers = data.get("workers")
        return s
