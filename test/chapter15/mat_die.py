from random import randint

class Die():
    """掷骰子"""

    def __init__(self,num_sides=6,times=50000):
        """初始化属性"""
        self.num_sides = num_sides
        self.times = times

    def create_x_label(self):
        """生成横坐标"""
        x_label = []
        for x in range(1,self.num_sides+1):
            x_label.append(x)
        return x_label

    def create_y_label(self):
        """生成纵坐标，计数"""
        # 掷骰子
        results = []
        for i in range(self.times):
            result = randint(1,self.num_sides)
            results.append(result)
        # 计数
        frequencies = []
        for value in range(1, self.num_sides + 1):
            frequency = results.count(value)
            frequencies.append(frequency)
        return frequencies
