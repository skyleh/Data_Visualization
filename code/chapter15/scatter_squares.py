import matplotlib.pyplot as plt


x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues ,edgecolors=None, s=40)

#设置图表标题及坐标轴
plt.title("Square Value",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

plt.axis([0,1001,0,1100000])

plt.show()
