#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygal
import json
from api_setting import Settings
from time_text import TimeExchange
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#获取json数据

data_setting = Settings()
filename = data_setting.music_sun
with open(filename,encoding='UTF-8') as f_obj:
    pop_data = json.load(f_obj)

#打印信息
print(pop_data['keyword'] + " has " + str(pop_data['totalnum']) + " songs!")
pop_dict = pop_data['list']
dates, descriptions = [], []
for message in pop_dict:
    try:
        time_change = TimeExchange(message['pubtime'])
        changed_time = time_change.ChangeTime()
        description = [
            {
                'name' : message['songname'],
                'singer': message['singername']
                'link' : message['songurl']
            }
        ]
    except:
        continue
    else:
        descriptions.append(description)
        dates.append(str(changed_time))

#绘图
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
#x轴坐标旋转45°
my_config.x_label_rotation = 45
#隐藏图例
my_config.show_legend = False
#设置标题字体大小
my_config.title_font_size = 24
#设置副字体大小
my_config.label_font_size = 14
#设置主标签字体大小
my_config.major_label_font_size = 18
#删除横坐标网格线
my_config.show_y_guides = False
#设置柱状图宽度
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)
chart.title = "Stefanie's Songs,by Year"
chart.add('', dates)

chart.render_to_file('Stefanie_song.svg')
