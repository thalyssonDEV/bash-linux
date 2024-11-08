import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'colors')))

from colors import *

class TerminalMessage():
  def __init__(self) -> None:
    pass

  def error(self, message: str) -> None:
    print(f"{LIGHT_RED}{message}\033{RESET}")
    
  def success(self, message: str) -> None:
    print(f"{LIGHT_GREEN}{message}{RESET}")