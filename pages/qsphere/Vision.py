#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common.Browser import Browser
from common import elePages


class Vision(object):
    def __init__(self):
        self.browser = Browser()

    def access_vision_page(self):
        self.browser.click_button(
            page=elePages.qsphere.Vision(),
            key=u'愿景'
        )

    def check_vision_page_title(self):
        vision_title = self.browser.get_element_text(
            page=elePages.qsphere.Vision(),
            key=u'标题'
        )
        assert vision_title == u'愿景', u'标题不正确'


if __name__ == '__main__':
    print('This is Vision page keywords')