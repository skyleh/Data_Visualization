#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Settings():
    """文件设置"""

    def __init__(self):
        """属性初始化"""
        self.url_github_python = 'https://api.github.com/search/repositories?q=language:python' \
                          '&sort=stars'
        self.hacker_news = 'https://hacker-news.firebaseio.com/v0/topstories.json'