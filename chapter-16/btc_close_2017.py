import json
import pygal
import math
from itertools import groupby

# 将数据加载到一个列表中
filepath = r"chapter-16\btc_close_2017.json"

with open(filepath) as f:
    # 从`file-like Object`中读取字符串并反序列化
    btc_data = json.load(f) # btc_data 是一个列表，每个元素是一个字典

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


# 绘制折线图
def draw_line(x_data, y_data, title, y_legend):
    """
    x_data 与 y_data 都是列表。在这里，两个列表的中的元素依次对应
    zip() 将这两个列表中依次对应的元素组成一个 tuple, 所有tuple组成一个列表
        例：x_data = [1, 1, 3], y_data = ['a', 'b', 'c']
        zip(x_data, y_data) return: [(1, 'a'), (1, 'b'), (3, 'c')]
    groupby 根据键函数来分组。键函数作用在上面返回的列表的元素上
    """
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        # print(x, y)
        y_list = [v for _, v in y] 
        xy_map.append([x, sum(y_list) / len(y_list)])
        
    """
    假设：xy_map = [[1, 23], [2, 24]]
    *xy_map => [1, 23], [2, 24]
    zip(*xy_map) => [(1, 2), (23, 24)]
    """
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值（￥）', '月日均值')
