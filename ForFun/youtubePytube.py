from pytube import YouTube
import os

def download_video(url, name):
  print(url, name)
  try:
    yt = YouTube(url)
    video = yt.streams.first()
    yt.set_filename(name)
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    print(curr_dir)
    video = yt.streams.filter(progressive = True, file_extension='mp4').order_by('resolution')[-1]
    video.download(curr_dir)

    return True

  except:
    return False