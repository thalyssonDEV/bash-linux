import os
import sys
import time
import psutil
import subprocess
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from TerminalMessage import TerminalMessage
stdout = TerminalMessage()

class Command:
  def __init__(self) -> None:
    pass

  def touch(self, attempt_command: str) -> None:
    command = attempt_command.strip().split()

    path = '../files/'
    file_name = command[1]
    full_path = os.path.join(path, file_name)

    os.makedirs(path, exist_ok=True)

    with open(full_path, "x"):
      pass
    stdout.success(f"touch: the file '{file_name}' was created successfully.")


  def echo(self, attempt_command: str) -> None:
    command = attempt_command.strip().split()

    path = '../files/'
    text_to_write = ' '.join(command[1:-2])
    file_redirect = command[-1]

    full_path = path + file_redirect

    if command[-2] == '>':
      with open(full_path, 'w') as file:
          file.write(text_to_write + '\n')

    elif command[-2] == '>>':
      with open(full_path, 'a') as file:
          file.write(text_to_write + '\n')


  def clear(self) -> None:
    os.system('clear')


  def exit(self) -> None:
    exit()


  def rm(self, attempt_command: str) -> None:
    command = attempt_command.strip().split()

    path = '../files/'
    name_file = command[1]
    full_path = path + name_file

    if os.path.isfile(full_path):
      os.remove(full_path)
      stdout.success(f"rm: '{name_file}' removed successfully")
    else:
      stdout.error(f"rm: cannot remove '{name_file}': No such file or directory")
    
    
  def mv(self, attempt_command) -> None:
    command = attempt_command.strip().split()

    path = '../files/'
    old_file_path = os.path.join(path, command[1])
    new_file_path = os.path.join(path, command[2])
    
    try:
      os.rename(old_file_path, new_file_path)

    except FileNotFoundError:
      stdout.error(f"mv: cannot rename '{command[1]}': No such file or directory")


  def top(self) -> None:
    print(' Monitoring System '.center(50, '-'))
    print(f'Uptime: {psutil.boot_time()}')

    cpu_percent = psutil.cpu_percent(interval=0.1)
    print(f"CPU usage: {cpu_percent}%")

    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Free Memory: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Memory Usage Percentage: {memory.percent}%")

    print("-" * 50)
    print("PID\tUser\t%CPU\t%MEM\tTime\tCommand")
    print("-" * 50)

    for proc in psutil.process_iter(['pid', 'username', 'cpu_percent', 'memory_percent', 'create_time', 'name']):
          try:
              print(f"{proc.info['pid']}\t{proc.info['username']}\t"
                      f"{proc.info['cpu_percent']:.1f}\t{proc.info['memory_percent']:.1f}\t"
                      f"{time.strftime('%H:%M:%S', time.gmtime(proc.info['create_time']))}\t"
                      f"{proc.info['name']}")
          except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
              pass
      
    print("-" * 50)


  def yt_dlp(self, attempt_command) -> None:
    command = attempt_command.strip().split()
    video_url = command[2]
      
    try:
      import yt_dlp

    except ImportError:
      stdout.error("yt-dlp library not found: install the package with the command 'pip install yt-dlp'")
      return 1
        
    if command[1] == 'mp4':
      sys.stderr = open(os.devnull, 'w')
      
      ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True
      }
      
      try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          ydl.download([video_url])
          stdout.success(f'Download Successful!')
          
      except Exception as e:
        stdout.error('Download Failed: URL not found.')

    # elif command[1] == 'mp3':
    #     sys.stderr = open(os.devnull, 'w')
        
    #     ydl_opts = {
    #         'format': 'bestaudio/best',
    #         'outtmpl': '%(title)s.%(ext)s',
    #         'postprocessors': [{
    #             'key': 'FFmpegAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192',
    #         }],
    #         'quiet': True
    #     }
        
    #     try:
    #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #             ydl.download([video_url])
    #             stdout.success(f'Download Successful! Audio saved as MP3.')
    #     except Exception as e:
    #       stdout.error(f'Download Failed: {str(e)}')

  def weather(self, attempt_command) -> None:
    command = attempt_command.strip().split()
    city = command[1]

    API_KEY = 'c9a21fc9b47eacdd32144b51149a37ba'
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    url = f"{base_url}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()

      city_name = data['name']
      temperature = data['main']['temp']
      humidity = data['main']['humidity']
      description = data['weather'][0]['description']
      wind_speed = data['wind']['speed']

      print(f"Clima em {city_name}:")
      print(f"Temperatura: {temperature}°C")
      print(f"Umidade: {humidity}%")
      print(f"Descrição: {description}")
      print(f"Velocidade do vento: {wind_speed * 3.6} Km/h")