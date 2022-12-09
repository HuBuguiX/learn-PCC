import matplotlib.pyplot as plt
from random_walk import RandomWalk

"""将随机漫步的值绘制出来"""
while True:
    # 创建一个 RandomWalk 实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples, s=1)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 突出起点和重点
    plt.scatter(0, 0, c='green', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', s=20)
    # plt.plot([0], [0], c='green', linewidth=5)

    # 设置每个坐标轴的取值范围
    # plt.axis([-350, 350, -350, 350])

    # 隐藏坐标轴
    # 这两行是书上的代码，有问题
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False) 
    plt.axis('off')

    plt.show()

    # keep_running = input("Make another walk? (y/n): ")
    # if keep_running == 'n':
    #     break
    break
