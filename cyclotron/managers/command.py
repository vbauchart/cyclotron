import subprocess

from cyclotron.managers import CriticalOperationException


class CommandManager(object):

    def __init__(self, command_line):
        self.command_line = command_line

    def exec_command(self, check_return=0):

        code = subprocess.call(self.command_line)

        if code != check_return:
            raise CriticalOperationException('Command %s exited with code %d'%(self.command_line, code))