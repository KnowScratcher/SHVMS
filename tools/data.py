import json
import os

data = {}
with open("./data.json","r",encoding="utf-8") as j:
        data = json.load(j)
def update():
    global data
    default = {"name": ""}
    with open("./data.json","r",encoding="utf-8") as j:
        data = json.load(j)

    for i in os.listdir("video"):
        name = "".join(i.split(".")[:-1])
        # print(name)
        if data.get(name,None) == None:
            data[name] = default.copy()
            data[name]["name"] = name
    with open("./data.json","w",encoding="utf-8") as j:
        json.dump(data,j)

def rename(key:str,value:str):
    global data
    with open("./data.json","r",encoding="utf-8") as j:
        data = json.load(j)
    if data.get(key,None) != None:
        data[key]["name"] = value
    else:
        return False
    with open("./data.json","w",encoding="utf-8") as j:
        json.dump(data,j)
    return True

def get(s):
    global data
    return data.get(s,None)