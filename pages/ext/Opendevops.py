#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common.Browser import Browser
from common import elePages


class Opendevops(object):
    def __init__(self):
        self.browser = Browser()

    def access_odo_page(self):
        self.browser.click_button(
            page=elePages.ext.Opendevops(),
            key=u'OpenDevOps'
        )

    def check_odo_title(self):
        odo_title = self.browser.get_element_text(
            page=elePages.ext.Opendevops(),
            key=u'标题'
        )
        assert odo_title == u'OpenDevOps', u'标题不正确'


if __name__ == '__main__':
    print('This is ODO page keywords')
