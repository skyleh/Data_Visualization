import requests
import pygal
from url_settings import Settings
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
url_setting = Settings()
url = url_setting.url_github_python
r = requests.get(url)
print("Status code:", r.status_code)

#将API响应存储在一个变量中
reponse_dict = r.json()
print("Total repositories:",reponse_dict['total_count'])

#研究仓库的信息
repo_dicts = reponse_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
#x轴左边旋转45°
my_config.x_label_rotation = 45
#不展示图例
my_config.show_legend = False
#设置标题字体，副标签和主标签字体大小
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
#缩短项目名称为15字符
my_config.truncate_label = 15
#隐藏图标水平线
my_config.show_y_guides = False
#设置自定义宽度
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')