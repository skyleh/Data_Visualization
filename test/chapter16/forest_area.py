#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import pygal.maps.world
from country import get_country_code
from setting import Settings
from pygal.style import RotateStyle

#从csv文件获取数据
data_settings = Settings()
filename = data_settings.forest_area
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)

    #创建一个包含国家码和森林面积的字典
    forest_areas = {}

    for row in reader:
        try:
            forest_area = int(float(row[29]))
            country_name = row[0]
        except ValueError:
            continue
        else:
            code = get_country_code(country_name)
            if code:
                forest_areas[code] = forest_area

#绘制世界地图
wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Forest Area in 2015,by Country'
wm.add('2015',forest_areas)

wm.render_to_file('forest_area_2015_1.svg')