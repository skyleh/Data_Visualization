from random import randint
class Die():
    """模拟掷筛子"""
    def __init__(self,num_sides=6):
        """初始化"""
        self.num_sides = num_sides

    def roll_die(self):
        return randint(1,self.num_sides)