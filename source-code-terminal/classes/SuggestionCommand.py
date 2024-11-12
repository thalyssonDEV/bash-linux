import platform
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes')))

from TerminalMessage import TerminalMessage

version_kernel = platform.uname()
stdout = TerminalMessage()

class SuggestionCommand:
    def __init__(self) -> None:
        self.commands_dict = {
            'touch',
            'rm',
            'exit', 
            'clear',
            'echo',
            'mv',
            'help',
            'top',
            'pip install yt-dlp',
            'pip uninstall yt-dlp'
        }

    def suggest_command(self, command: str) -> None:
        matching_commands = []

        if len(command) < 2:
            return None
        
        else:
            for cmd in self.commands_dict:
                if cmd.startswith(command[:2]):
                    matching_commands.append(cmd)

            if matching_commands:
                stdout.error(", did you mean:")
                for cmd in matching_commands:
                    system_info = version_kernel.system
                    node_info = version_kernel.node
                    print(f"\tcommand '{cmd}' from {id(cmd)} (system='{system_info}', node='{node_info}')")

