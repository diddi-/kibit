from icmplib import ping

from kibit.modules.module import Module
from kibit.modules.ping.ping_arguments import PingArguments


class Ping(Module):
    name = "ping"
    arguments = PingArguments

    def run(self, args: PingArguments):
        result = ping(args.destination, count=args.count, privileged=False)
        return result.packet_loss == 0
