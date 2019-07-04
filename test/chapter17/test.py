#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from api_setting import Settings
from time_text import TimeExchange


data_setting = Settings()
filename = data_setting.music_sun
with open(filename, encoding='UTF-8') as f_obj:
    pop_data = json.load(f_obj)

pop_dict = pop_data['list']

#datas = []
names, songs = [], []
for message in pop_dict:
    #pubdate = str(message['pubtime'])
    #print(pubdate)
    #time_change = TimeExchange(message['pubtime'])
    #changed_time = time_change.ChangeTime()
    #print(changed_time)
    name = message['singername']
    song = message['songname']
    names.append(name)
    songs.append(song)
print(names)
print(songs)
