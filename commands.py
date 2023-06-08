from ranger.api.commands import Command
from pathlib import Path
from subprocess import run
from os import environ


class launch_new_workspace_with_cwd(Command):
    def execute(self):
        home = environ["HOME"]
        selection = Path(self.fm.thisfile.path)
        workspace_name = selection.parts[-1]
        run(
            [
                "sh",
                f"{home}/.config/ranger/create_new_workspace.sh",
                f"{str(selection)}",
                f"{workspace_name}",
            ]
        )
