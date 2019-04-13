# -*- coding: utf-8 -*-
import os, json, codecs

VALID_TYPES = ["Generic", "Share"]

# https://stackoverflow.com/a/52494169/5257483
def parse_obj(obj):
    for key in obj:
        if isinstance(obj[key], str):
            obj[key] = obj[key].encode('latin_1').decode('utf-8')
        elif isinstance(obj[key], list):
            obj[key] = list(map(lambda x: x if type(x) != str else x.encode('latin_1').decode('utf-8'), obj[key]))
        pass
    return obj

name = input("Enter your full name on Facebook >")


prefix = 'messages/inbox'
threads = next(os.walk(prefix))[1]


c = 0

with open('corpus.txt', 'w+') as f:
    for thread in threads:
        # print(thread)
        with open(prefix + '/' + thread + '/message_1.json') as messages:
            messages = json.load(messages, object_hook=parse_obj)["messages"]
            for message in messages:
                if message["sender_name"] == name and "content" in message and "Say hi to your new Facebook friend" not in message["content"]:
                    c += 1
                    f.write(message["content"] + "\n")

print("Found", c, "messages")