import subprocess
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from TerminalMessage import TerminalMessage
stdout = TerminalMessage()

class Dependencies:
    def __init__(self) -> None:
        pass

    # pip commands
    def pip_install_yt_dlp(self):
        try:
            with open(os.devnull, 'w') as devnull:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yt-dlp'], stdout=devnull, stderr=devnull)
                stdout.success('yt-dlp installation successful!')

        except subprocess.CalledProcessError as e:
            stdout.error('error when trying to install yt-dlp, check system permissions!')
            raise e

    def pip_uninstall_yt_dlp(self):
        try:
            with open(os.devnull, 'w') as devnull:
                subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'yt-dlp', '-y'], stdout=devnull, stderr=devnull)
                stdout.success('yt-dlp successfully uninstalled!')

        except subprocess.CalledProcessError as e:
            stdout.error('error when trying to install yt-dlp!')
            raise e


