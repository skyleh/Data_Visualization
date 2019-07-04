from random import choice

class RandomWalk():
    """模拟随机漫步"""

    def __init__(self,num_points=20000):
        """一些初始化"""
        self.num_points = num_points

        #设置起始点为原点
        self.x_values = [0]
        self.y_values = [0]

    def fill_rw(self):
        """填充漫步点"""
        while len(self.x_values) < self.num_points:
            #设置步长，步距
            x_direction = choice([1, -1])
            x_distance = choice([0,1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_diatance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_diatance

            #获取下一点
            next_x = self.x_values[-1] + x_step
            next_y  =self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

