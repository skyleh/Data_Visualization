from random import randint

class Dies():
    """掷骰子"""

    def __init__(self,num_sides=6):
        """初始化"""
        self.num_sides = num_sides

    def roll_dies(self):
        """掷骰子"""

        return randint(1,self.num_sides)

    def create_x_lebels(self):
        """自动生成x轴坐标"""
        x_lebels = []
        for x in range(1,self.num_sides+1):
            x_lebels.append(str(x))
        return x_lebels
