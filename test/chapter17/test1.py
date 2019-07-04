#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time



def ChangeTime(timeStap):
    timeArray = time.localtime(timeStap)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


time_change = ChangeTime(1160150400)
print(time_change)