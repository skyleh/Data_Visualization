#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pygal
from setting import Settings
from country import get_country_code
from pygal.style import LightGreenStyle

#获取json数据
data_settings = Settings()
filename = data_settings.gdp
with open(filename) as f_obj:
    pop_data = json.load(f_obj)
#创建GDP字典
cc_gdp = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2016':
        country_name = pop_dict['Country Name']
        gdp_value = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp_value

#创建世界地图实例
wm_style = LightGreenStyle
wm = pygal.maps.world.World(style = wm_style)
#wm = pygal.Worldmap(style = wm_style)

wm.title = "World's GDP in 2016,by Country"
wm.add('GDP',cc_gdp)

wm.render_to_file('world_gdp.svg')



