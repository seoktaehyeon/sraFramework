#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common.Browser import Browser
from common import elePages


class Api(object):
    def __init__(self):
        self.browser = Browser()

    def access_api_page(self):
        self.browser.click_button(
            page=elePages.about.Api(),
            key=u'接口文档'
        )

    def check_api_page_title(self):
        api_title = self.browser.get_element_text(
            page=elePages.about.Api(),
            key=u'接口文档'
        )
        assert api_title == u'接口文档', u'标题不正确'

    def input_swagger_json_path(self, path: str):
        self.browser.input_text(
            page=elePages.about.Api(),
            key=u'SwaggerInput',
            value=path
        )

    def click_explore_button(self):
        self.browser.click_button(
            page=elePages.about.Api(),
            key=u'SwaggerExplore'
        )


if __name__ == '__main__':
    print('This is API page keywords')