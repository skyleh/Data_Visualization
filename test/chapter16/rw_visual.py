import matplotlib.pyplot as plt
from randomwalk import RandomWalk

while True:
    #创建一个随机漫步实例
    rw = RandomWalk()
    rw.fill_rw()

    #开始绘图
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greys,
                s=1)

    #突出起点和终点
    plt.scatter(0, 0, c='green', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=20)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another rw?(y/n)")
    if keep_running == 'n':
        break