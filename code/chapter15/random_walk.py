from random import choice

class RandowWalk():
    """模拟随机漫步"""

    def __init__(self,num_points=5000):
        """初始化随机漫步属性（漫步点数）"""
        self.num_points = num_points

        #设置随机漫步起点
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #点数少于5000，不断漫步
        while len(self.x_values) < self.num_points:

            #决定前进方向，前进步长
            x_direction = choice([1,-1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #排除原地踏步情况
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)