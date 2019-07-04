from random import choice

class RandomWalk():
    """模拟随机漫步"""

    def __init__(self,num_points=5000):
        """初始化一些属性"""
        self.num_points = num_points

        #设置起始点
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """获取移动方向和距离"""
        move_direction = choice([1, -1])
        move_dictance = choice([0, 1, 2, 3, 4])
        move_step = move_direction * move_dictance
        return move_step

    def fill_walk(self):
        """填充随机漫步点"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            #排除原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #获取下一个值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)