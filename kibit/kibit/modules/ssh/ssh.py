import paramiko

from kibit.modules.module import Module
from kibit.modules.ssh.ssh_arguments import SshArguments


class Ssh(Module):
    name = "ssh"
    arguments = SshArguments

    def run(self, args: SshArguments) -> bool:
        client = paramiko.SSHClient()
        client.connect(args.host)
        return True
