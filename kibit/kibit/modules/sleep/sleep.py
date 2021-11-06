import random
import time

from kibit.modules.module import Module
from kibit.modules.sleep.sleep_arguments import SleepArguments


class Sleep(Module):
    name = "sleep"
    arguments = SleepArguments

    def run(self, args: SleepArguments):
        s = random.randint(args.min_sec, args.max_sec)
        time.sleep(s)
        return True
