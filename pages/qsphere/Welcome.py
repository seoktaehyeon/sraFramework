#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common.Browser import Browser
import os


class Welcome(object):
    def __init__(self):
        self.browser = Browser()

    def access_homepage(self, url: str):
        self.browser.access(url)

    def check_page_title(self, title: str):
        assert self.browser.check_title(title), u'未能正常打开网页'

    def close_browser(self):
        self.browser.close_chrome()


if __name__ == '__main__':
    print('This is Welcome page keywords')
