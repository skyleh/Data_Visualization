import json
import pygal
from pygal.style import LightGreenStyle
from settings import Settings
from country_codes import get_country_code


#获取json数据
data_settings = Settings()
filename = data_settings.population_json
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

#创建人口数据字典
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population
#根据人口数量，将所有国家分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
#查看每个分组有多少国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = LightGreenStyle
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)

wm.render_to_file('world_population.svg')