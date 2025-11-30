from pytubefix import YouTube
from moviepy.editor import AudioFileClip
import os

video_url = "" # youtube URL here

try:
    yt = YouTube(video_url)
    print("Video title:", yt.title)

    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream is None:
        raise RuntimeError("Nenhum stream de áudio encontrado para esse vídeo.")

    print("Downloading audio file: " + yt.title)
    audio_file = audio_stream.download()
    print("File downloaded:", audio_file)

    base, _ = os.path.splitext(audio_file)
    mp3_file = base + ".mp3"

    print("Converting to mp3...")
    audio = AudioFileClip(audio_file)
    audio.write_audiofile(mp3_file)

    audio.close()
    os.remove(audio_file)

    os.system(f'demucs "{mp3_file}"')

    os.remove(mp3_file)

    print("Downloaded and separated song!")

except Exception as e:
    print("Error:", e)
