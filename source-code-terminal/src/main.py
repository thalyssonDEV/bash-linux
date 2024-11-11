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

def update_top(terminal: Command) -> None:
  terminal.top()

def main() -> None:
  os.system('clear')
  stdout = TerminalMessage() # Instância da classe TerminalMessage
  terminal = Command() # Intância da classe Command
  suggest = SuggestionCommand() # Instância da classe SuggestCommand
  
  while True:
    try:
      attempt_command = input('> ')
      if not attempt_command:
        continue

      readline.add_history(attempt_command)

      code_terminal_command = Assignments.check_command(attempt_command)
    
      match code_terminal_command:
        case 1:
          terminal.touch(attempt_command)
          
        case 2:
          terminal.clear()

        case 3:
          terminal.echo(attempt_command)

        case 4:
          terminal.rm(attempt_command)

        case 5:
          terminal.mv(attempt_command)
        
        case 6:
          Documentation.show_help()

        case 7:
          top_thread = threading.Thread(target=update_top, args=(terminal,), daemon=True)
          top_thread.start()

        case 8:
          terminal.yt_dlp(attempt_command)

        case 0:
          terminal.exit()

        case _:
          command = attempt_command.strip().split()
          stdout.error(f"{command[0]}: command not found")
          suggest.suggest_command(command[0])

    except KeyboardInterrupt:
      break

main()