from pytube import YouTube
from moviepy.editor import *
import os

def download_video(url, title):
    try:
        yt = YouTube(url)

        # Создание папки data, если она не существует
        if not os.path.exists('data'):
            os.makedirs('data')

        # Скачивание видео
        video = yt.streams.get_highest_resolution()
        video_file = os.path.join('data', f"{title}.mp4")
        video.download(output_path='data', filename=f"{title}.mp4")

        # Извлечение аудиопотока
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = os.path.join('data', f"temp_{title}.mp4")
        audio_stream.download(output_path='data', filename=f"temp_{title}.mp4")

        # Конвертация аудио в MP3
        audio_mp3 = os.path.join('data', f"{title}.mp3")
        audio_clip = AudioFileClip(audio_file)
        audio_clip.write_audiofile(audio_mp3)
        audio_clip.close()

        os.remove(audio_file)  # Удаление временного аудиофайла
        print(f"Успешно скачано видео: {video_file}")
        print(f"Успешно скачано и конвертировано аудио: {audio_mp3}")

    except Exception as e:
        print(f"Произошла ошибка с URL {url}: {e}")

def download_videos(urls):
    for url, title in urls:
        download_video(url, title)

if __name__ == "__main__":
    urls = [
        ("https://www.youtube.com/watch?v=SjZ98JOA4tc", "короткое_Видео_1")
    ]
    download_videos(urls)
