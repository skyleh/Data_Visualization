#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Settings():
    """API设置"""

    def __init__(self):
        """API地址初始化"""

        self.music_api = 'http://cgi.music.soso.com/fcgi-bin/' \
                         'fcg_search_xmldata.q?source=10&w=%E5%AD%99%E7%87%95%E5%A7%BF&perpage=500&ie=utf-8'
        self.music_sun = 'G:/workstation/py_workstation/Data_Visualization/test' \
                         '/chapter17/json/music_sun.json'
