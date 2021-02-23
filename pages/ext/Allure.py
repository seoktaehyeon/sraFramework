#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common.Browser import Browser
from common import elePages
from time import sleep


class Allure(object):
    def __init__(self):
        self.browser = Browser()

    def access_allure_page(self):
        self.browser.click_button(
            page=elePages.ext.Allure(),
            key=u'Allure'
        )

    def check_allure_page_title(self):
        allure_title = self.browser.get_element_text(
            page=elePages.ext.Allure(),
            key=u'标题'
        )
        assert allure_title == u'Allure 框架中文手册', u'标题不正确'

    def click_menu(self, menu: str):
        self.browser.click_button(
            page=elePages.ext.Allure(),
            key=menu
        )


if __name__ == '__main__':
    print('This is Allure page keywords')
