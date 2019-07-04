#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

class TimeExchange():
    """时间转换类"""

    def __init__(self,timeStap):
        self.timeStap = timeStap


    def ChangeTime(self):
        timeArray = time.localtime(self.timeStap)
        otherStyleTime = time.strftime("%Y", timeArray)
        return otherStyleTime


# time_change = TimeExchange(1160150400)
# changed_time = time_change.ChangeTime()
# print(changed_time)