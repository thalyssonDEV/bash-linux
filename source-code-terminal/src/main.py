import sys
import os
import readline
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs')))

from Documentation import Documentation
from Assignments import Assignments
from Command import Command
from TerminalMessage import TerminalMessage
from SuggestionCommand import SuggestionCommand
from Dependencies import Dependencies

def update_top(terminal: Command) -> None:
  terminal.top()

def main() -> None:
  os.system('clear')
  stdout = TerminalMessage() # Instância da classe TerminalMessage
  terminal = Command() # Intância da classe Command
  suggest = SuggestionCommand() # Instância da classe SuggestCommand
  terminal_dependencies = Dependencies() # Instãncia da classe Dependencies
  
  while True:
    try:
      attempt_command = input('> ')
      if not attempt_command:
        continue

      readline.add_history(attempt_command)

      code_terminal_command = Assignments.check_command(attempt_command)
    
      match code_terminal_command:

        case 'touch':
          terminal.touch(attempt_command)
          
        case 'clear':
          terminal.clear()

        case 'echo':
          terminal.echo(attempt_command)

        case 'rm':
          terminal.rm(attempt_command)

        case 'mv':
          terminal.mv(attempt_command)
        
        case 'help':
          Documentation.show_help()

        case 'top':
          top_thread = threading.Thread(target=update_top, args=(terminal,), daemon=True)
          top_thread.start()

        case 'yt-dlp':
          terminal.yt_dlp(attempt_command)

        case 'exit':
          terminal.exit()

        case 'weather':
          terminal.weather(attempt_command)

        case 1:
          terminal_dependencies.pip_install_yt_dlp()
        case -1:
          terminal_dependencies.pip_uninstall_yt_dlp()
       

        case _:
          command = attempt_command.strip().split()
          stdout.error(f"{command[0]}: command not found")
          suggest.suggest_command(command[0])

    except KeyboardInterrupt:
      break

main()