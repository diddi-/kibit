import os
from typing import List

from colorama import Cursor, Fore

from kibit.tasks.task import Task
from kibit.tasks.task_result import TaskResult


class ProgressEntry:
    def __init__(self, task: Task):
        self.task = task
        self.status = "Waiting"

class Progress:
    CLR = "\x1B[0K"

    def __init__(self):
        self.entries: List[ProgressEntry] = []
        self.cursor_line = 0

    def _move_up(self, lines):
        if self.cursor_line - lines < 0:
            raise ValueError("Can't move up beyond line 0")
        print(Cursor.UP(lines), end="")
        self.cursor_line -= lines

    def _move_down(self, lines):
        if self.cursor_line + lines > len(self.entries):
            raise ValueError(f"Can't move down beyond line {len(self.entries)}")
        print(Cursor.DOWN(lines), end="")
        self.cursor_line += lines

    def add_task(self, task: Task):
        entry = ProgressEntry(task)
        self.entries.append(entry)
        self.print_entry(entry)

    def print_entry(self, entry: ProgressEntry):
        print(f"* {entry.task.name}... {entry.status}{self.CLR}")
        self.cursor_line += 1

    def redraw(self):
        self._move_up(self.cursor_line)
        for e in self.entries:
            self.print_entry(e)

    def update(self, result: TaskResult):
        for e in self.entries:
            if e.task.task_id != result.task_id:
                continue
            e.status = f"{Fore.GREEN}OK{Fore.RESET}" if result.success else f"{Fore.RED}FAIL{Fore.RESET}"
        self.redraw()
