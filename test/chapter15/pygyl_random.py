import matplotlib.pyplot as plt
from pygal_rw_visual import RandomWalk

#只要程序为活跃状态就不断模拟随机漫步
while True:
    #创建一个随机漫步实例，并将其包含的点绘制
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, s=0.5)

    #突出显示起点和终点
    plt.scatter(0,0,c='green',s=20)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=20)

    #省略坐标轴
    plt.axes().xaxis.set_visible(False)
    plt.axes().yaxis.set_visible(False)

    plt.show()

    #循环重绘
    keep_running = input("Make another randowwalk?(y/n)")
    if keep_running == 'n':
        break