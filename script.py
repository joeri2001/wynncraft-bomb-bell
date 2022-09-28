from email import header
import time
import requests

# replace *path to folder* with the path to your .minecraft\logs\latest.log folder
infile = r"*path to folder*"

array = []
bomb_bell_check = ["[Bomb Bell]"]

last_bomb = any

i = 1
while i > 0:
    with open(infile) as f:
        f = f.readlines()

    for line in f:
        for phrase in bomb_bell_check:
            if phrase in line:
                array.append(line.replace(" [Client thread/INFO] [chat]: [CHAT] ", " "))
                break

    last_element = array[-1]

    if len(last_element) < 100:
        if last_bomb != last_element:
            last_bomb = last_element
            payload = {
                'content': last_element
            }

            # open network tab > send a message in the discord chat > go to response header > copy the autorization token > paste the token instead of *token*
            header = {
                'authorization': '*token*'
            }

            # put channel id instead of *channel id*
            r = requests.post("https://discord.com/api/v9/channels/*channel id*/messages", data=payload, headers=header)

    time.sleep(1)