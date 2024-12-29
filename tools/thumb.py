from moviepy import *
import os

def update():
    for i in os.listdir("video"):
        if not os.path.exists(f"thumbnail/{''.join(i.split('.')[:-1])}.jpg"):
            try:
                create("".join(i.split(".")[:-1]))
            except:pass

def create(name):
    clip = VideoFileClip(f"video/{name}.mp4")
    clip.save_frame(f"thumbnail/{name}.jpg",t=1.00)