import paramiko

from kibit.modules.module import Module
from kibit.modules.ssh.ssh_arguments import SshArguments


class Ssh(Module):
    name = "ssh"
    arguments = SshArguments

    def run(self, args: SshArguments) -> bool:
        transport = paramiko.Transport(args.host)
        transport.connect()
        key = transport.get_remote_server_key()
        transport.close()
        return key.get_fingerprint() is not None
