import matplotlib.pyplot as plt
from random_walks import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    #设置绘图窗口尺寸
    plt.figure(dpi=128,figsize=(20,10))
    point_number = list(range(rw.num_points))
    #plt.plot(rw.x_values,rw.y_values,linewidth=5)
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, s=1)
    #重新绘制起点和终点
    plt.scatter(0,0,c='green',s=30)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=30)
    #消除坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another randomwalk?(y/n)")
    if keep_running == 'n':
        break