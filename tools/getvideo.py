import random
import os
from tools.data import get

def format() -> str:
    length = len(os.listdir("video"))
    data = []
    choice = random.sample(["".join(x.split(".")[:-1]) for x in os.listdir("video")],min(length,60))
    for i in choice:
        data.append({"title":get(i)["name"],"id":i})
    return data