import csv
from matplotlib import pyplot as plt
from datetime import datetime


# 从文件中获取日期、最高气温和最低气温
filepath = r"chapter-16\death_valley_2014.csv"
with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    # 将列表中每一个元素的索引及其值打印出来
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

# 根据数据绘制图形
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.4)
plt.plot(dates, lows, c='blue', alpha=0.4)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()