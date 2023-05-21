from ranger.api.commands import Command
from subprocess import run
from os import environ


class launch_new_workspace_with_cwd(Command):
    def execute(self):
        home = environ["HOME"]
        selection = self.fm.thisfile.path
        run(["sh", f"{home}/.config/ranger/get_workspace_num.sh", f"{selection}"])
