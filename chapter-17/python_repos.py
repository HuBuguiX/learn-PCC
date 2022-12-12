import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将 API 响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
# 与书本代码与最新 pygal 不兼容，参照 https://blog.csdn.net/weixin_43091089/article/details/99792892
my_config = pygal.Config()
my_config.style = LS('#333366', base_style=LCS)
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.style.title_font_size = 24
my_config.style.label_font_size = 14
my_config.style.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')