import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',  # Escolhe a melhor qualidade disponível
        'outtmpl': '%(title)s.%(ext)s',  # Salva o vídeo com o nome do título
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Exemplo de uso
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Substitua com a URL do vídeo
download_video(url)

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Baixa o melhor áudio disponível
        'outtmpl': '%(title)s.%(ext)s',  # Salva o arquivo com o nome do título
        'postprocessors': [{
            'key': 'FFmpegAudio',
            'preferredcodec': 'mp3',  # Converte para MP3
            'preferredquality': '192',  # Define a qualidade do áudio
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Exemplo de uso
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Substitua com a URL do vídeo
download_audio(url)
