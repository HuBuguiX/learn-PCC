from die import Die
import pygal

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果。计算所有可能出现的情况。计算每个点数出现的频率
frequencies = [] # 依次存储每种情况出现的概率
points = [] # 存储所有可能出现的情况
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    points.append(value)
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."

x_labels = list(map(str,points))
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

