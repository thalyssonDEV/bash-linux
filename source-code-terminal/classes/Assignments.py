class Assignments:
  def __init__(self) -> None:
    pass

  @staticmethod
  def check_command(attempt_command: str):
    command = attempt_command.strip().split()

    if command[0] == 'touch' and len(command) == 2:
      return 1

    elif command[0] == 'clear' and len(command) == 1:
      return 2

    elif command[0] == 'echo' and len(command) >= 4 and (command[-2] == '>' or command[-2] == '>>'):
      return 3

    elif command[0] == 'rm' and len(command) == 2:
      return 4

    elif command[0] == 'exit' and len(command) == 1:
      return 0
    
    elif command[0] == 'mv' and len(command) == 3:
      return 5
    
    elif command[0] == 'help' and len(command) == 1:
      return 6

    elif command[0] == 'top' and len(command) == 1:
      return 7

    elif (command[0] == 'yt-dlp' and len(command) == 3) and (command[1] == 'mp3' or command[1] == 'mp4'):
      return 8