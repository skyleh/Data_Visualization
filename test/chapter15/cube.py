import matplotlib.pyplot as plt

x_values = list(range(1,500))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Greens,
            edgecolors=None, s=40)

#设置图表标题及坐标轴
plt.title("Cude", fontsize=24)
plt.xlabel("Values",fontsize=14)
plt.ylabel("Cude of Value",fontsize=14)

#设置坐标轴字体大小
plt.tick_params(axis='both', labelsize=14)

#设置坐标轴区间
plt.axis([0,50,0,5000])

#绘图
plt.show()