import random
import os
from tools.data import get

def format() -> str:
    length = len(os.listdir("video"))
    data = []
    choice = random.sample(["".join(x.split(".")[:-1]) for x in os.listdir("video")],min(length,60))
    for i in choice:
        data.append({"title":get(i)["name"],"id":i}) # type: ignore
    return data # type: ignore

def search(query:str) -> str:
    sample = ["".join(x.split(".")[:-1]) for x in os.listdir("video") if (query.lower() in "".join(x.split(".")[:-1]).lower() or query.lower() in get("".join(x.split(".")[:-1]))["name"].lower())] # type: ignore
    data = []
    choice = random.sample(sample,min(len(sample),60))
    for i in choice:
        data.append({"title":get(i)["name"],"id":i}) # type: ignore
    return data # type: ignore
