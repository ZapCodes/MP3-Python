from ast import If
import pytube as pt
from pytube import YouTube
import os
import youtube_dl
import shutil







def dircreate():
    path2 = 'MP3'
    if not os.path.exists(path2):
        os.umask(0)
        os.makedirs(path2,0o777)
        print("Directory in windows created")


def url():


    video_url = input("ENTER VIDEO URL HERE: ")
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        dircreate()
        file = ydl.download([video_info['webpage_url']])
        shutil.move(filename, 'MP3')
        
    print("Download complete... {}".format(filename))



