class Assignments:
  def __init__(self) -> None:
    pass

  @staticmethod
  def check_command(attempt_command: str):
    command = attempt_command.strip().split()

    if command[0] == 'touch' and len(command) == 2:
      return 'touch'

    elif command[0] == 'clear' and len(command) == 1:
      return 'clear'

    elif command[0] == 'echo' and len(command) >= 4 and (command[-2] == '>' or command[-2] == '>>'):
      return 'echo'

    elif command[0] == 'rm' and len(command) == 2:
      return 'rm'

    elif command[0] == 'exit' and len(command) == 1:
      return 'exit'
    
    elif command[0] == 'mv' and len(command) == 3:
      return 'mv'
    
    elif command[0] == 'help' and len(command) == 1:
      return 'help'

    elif command[0] == 'top' and len(command) == 1:
      return 'top'

    # REVISAR
    elif (command[0] == 'yt-dlp' and len(command) == 3) and (command[1] == 'mp3' or command[1] == 'mp4'):
      return 'yt-dlp'

    # REVISAR
    elif command[0] == 'weather' and len(command) == 2:
      return 'weather'




    elif command[0] == 'pip' and len(command) == 3:
      if command[1] == 'install' and command[2] == 'yt-dlp':
        return 1
      elif command[1] == 'uninstall' and command[2] == 'yt-dlp':
        return -1