from mat_die import Die
import matplotlib.pyplot as plt

die = Die()
x_label = die.create_x_label()
y_label = die.create_y_label()

#绘图
plt.plot(x_label, y_label, linewidth=5)

#设置图表标题，坐标轴
plt.title("Result of rolling a D6 1000 times",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Frequencies of Result",fontsize=14)

#设置坐标轴大小
plt.tick_params(axis='both', labelsize=14)
plt.show()