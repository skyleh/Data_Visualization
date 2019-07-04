from die import Die
import pygal

#创建一枚六面的筛子
die_1 = Die()
die_2 = Die(10)
results = []
#掷10000次骰子
for num in range(50000):
    result = die_1.roll_die() + die_2.roll_die()
    results.append(result)

#统计点数的数量
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for number in range(2,max_result+1):
    frequency = results.count(number)
    frequencies.append(frequency)
    
#数据可视化
hist = pygal.Bar()

hist.title = "Result of rolling a D6 and a D10 50000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('G:/workstation/py_workstation/Data_Visualization/code/chapter15/results/die_visual.svg')