import pygal
import requests
from url_settings import Settings
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url_setting = Settings()
url = url_setting.url_github_python
r = requests.get(url)
print("Status code:",r.status_code)

#获取api数据
reponse_dict = r.json()
print("Total repositories:",reponse_dict['total_count'])

#查看仓库信息
repo_dicts = reponse_dict['items']
print("Number of items:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

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

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
