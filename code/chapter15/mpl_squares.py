import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

#设置图表标题及坐标轴
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()