from dies import Dies
import pygal

#创建一个骰子
die_1 = Dies()
die_2 = Dies()
#掷骰子10000次
results = []
for number in range(10000):
    result = die_1.roll_dies() * die_2.roll_dies()
    results.append(result)

#计数
frequencies = []
max_sides = die_1.num_sides * die_2.num_sides
for value in range(1,max_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#结果可视化
hist = pygal.Bar()
hist.title = "Result of rolling two D6 10000 times"
hist.x_labels = die_1.create_x_lebels()
hist.x_title = "Values"
hist.y_title = "Frequency of Result"

hist.add("D6",frequencies)
hist.render_to_file('G:/workstation/py_workstation/Data_Visualization/test/chapter15/results/die_visual.svg')