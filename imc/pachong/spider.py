# coding:utf-8
# -*- coding: utf-8 -*-
from urllib import request
import re


# 断点调试

class Spider():
    url = "https://www.douyu.com/g_LOL"
    root_pattern = '<div class="DyListCover-info">[\s\S]*?</div>'


    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls)
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        print(root_html[0])
        a = 1


    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()
