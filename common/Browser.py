#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: v.stone@163.com

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidElementStateException, ElementClickInterceptedException
import yaml
import json
import os
from time import sleep
from datetime import datetime
from robot.api import logger
import allure


def launch_chrome(width: int = 1920, height: int = 1200):
    """
    打开浏览器, debug 模式下 UI 可见且窗口最大化，CI 环境中 headless 并窗口 1920*1200
    :param width: default is 1920
    :param height: default is 1200
    :return:
    """
    with open(os.getenv('RF_VAR_FILE'), 'r', encoding='utf-8') as f:
        _debug = yaml.full_load(f.read()).get('RF_DEBUG')
    _opts = webdriver.ChromeOptions()
    _opts.add_argument('-lang=zh-cn')
    if _debug is True:
        print(u'启用可调试的常规模式')
        _browser = webdriver.Chrome(options=_opts)
        _browser.maximize_window()
    else:
        print(u'启用CI环境下的无头模式')
        _opts.add_argument('--headless')
        _opts.add_argument('--no-sandbox')
        _browser = webdriver.Chrome(options=_opts)
        _browser.set_window_size(width, height)
    if os.getenv('RF_PWD'):
        with open(os.path.join(os.getenv('RF_PWD'), 'output', 'browser.json'), 'w') as f:
            f.write(json.dumps(_browser.capabilities))
    return _browser


class Browser(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            cls._instance.browser = launch_chrome()
        elif not hasattr(cls._instance, 'browser'):
            cls._instance.browser = launch_chrome()
        return cls._instance

    def close_chrome(self):
        """
        关闭浏览器
        :return:
        """
        print(u'关闭浏览器')
        self.browser.close()

    @staticmethod
    def get_ele_xpath(ele_menu, ele_page, ele_name):
        """
        获取元素的 XPATH
        :param ele_menu:
        :param ele_page:
        :param ele_name:
        :return:
        """
        ele_yml_dir = os.path.join(
            os.getenv('RF_PWD'),
            'elements'
        )
        assert os.path.exists(ele_yml_dir), u'目录 %s 不存在' % ele_yml_dir
        yml_file_path = os.path.join(
            ele_yml_dir,
            ele_menu,
            '%s.yaml' % ele_page
        )
        assert os.path.exists(yml_file_path), u'文件 %s 不存在' % yml_file_path
        with open(yml_file_path, 'r', encoding='utf-8') as f:
            xpath = yaml.full_load(f.read()).get(ele_name)
        assert type(xpath) is str, u'元素 %s 的 xpath 未定义， 请检查 elements/%s/%s.yaml' % (ele_name, ele_menu, ele_page)
        print(u'元素 %s 的 xpath:%s' % (ele_name, xpath))
        return xpath

    def access(self, url: str):
        """
        访问网址
        :param url:
        :return:
        """
        print(u'访问 %s' % url)
        self.browser.get(url)

    def _find_ele(self, xpath: str):
        """
        查找元素
        :param xpath:
        :return:
        """
        for i in range(1, 10):
            print(u'\t尝试寻找元素 [%s/10] %s' % (i, xpath))
            try:
                return self.browser.find_element_by_xpath(xpath)
            except NoSuchElementException:
                sleep(1)
        raise NoSuchElementException(u'页面上未找到该元素')

    def screenshot(self, log_level: str = 'warn'):
        _path = os.path.join(os.getenv('RF_PWD'), 'output', 'attach')
        if os.path.exists(_path) is False:
            os.makedirs(_path)
        _png_name = '%s.png' % str(datetime.now().timestamp()).replace('.', '')
        self.browser.get_screenshot_as_file(os.path.join(_path, _png_name))
        if os.getenv('RF_REPORT_TYPE').lower() in ["local-allure", "jenkins-allure"]:
            allure.attach.file(source=os.path.join(_path, _png_name), attachment_type=allure.attachment_type.PNG)
        # elif os.getenv('RF_REPORT_TYPE').lower() in ["local-html"]:
        else:
            _msg = '<a href="./attach/%s"><img src="./attach/%s" width="800px"></a>' % (_png_name, _png_name)
            if log_level == 'info':
                logger.info(msg=_msg, html=True)
            elif log_level == 'error':
                logger.error(msg=_msg, html=True)
            else:
                logger.warn(msg=_msg, html=True)
        return True

    def click_button(self, page: dict, key: str):
        """
        点击按钮
        :param page: 页面 {'menu': '', 'page': ''}
        :param key: 元素名称
        :return:
        """
        print(u'点击 %s' % key)
        xpath = self.get_ele_xpath(page['menu'], page['page'], key)
        ele = self._find_ele(xpath)
        for i in range(1, 10):
            try:
                ele.click()
                self.screenshot(log_level='info')
                print(u'点击成功')
                return True
            except ElementClickInterceptedException:
                self.screenshot(log_level='warn')
                sleep(1)
        self.screenshot(log_level='error')
        raise ElementClickInterceptedException

    def input_text(self, page: dict, key: str, value: str):
        """
        输入内容
        :param page: 页面
        :param page: 页面 {'menu': '', 'page': ''}
        :param key: 元素
        :param value: 输入内容
        :return:
        """
        print(u'在 %s 中输入 %s' % (key, value))
        xpath = self.get_ele_xpath(page['menu'], page['page'], key)
        ele = self._find_ele(xpath)
        for i in range(1, 10):
            try:
                ele.clear()
                ele.send_keys(value)
                self.screenshot(log_level='info')
                print(u'输入成功')
                return True
            except InvalidElementStateException:
                self.screenshot(log_level='warn')
                sleep(1)
        self.screenshot(log_level='error')
        raise InvalidElementStateException

    def check_title(self, title: str):
        """
        检查网页标题
        :param title:
        :return:
        """
        print(u'检查网页标题 %s' % title)
        self.screenshot(log_level='info')
        assert self.browser.title == title, u'标题实际为 %s' % self.browser.title

    def upload_file(self, page: dict, key: str, value: str):
        """
        上传文件
        :param page:
        :param key:
        :param value:
        :return:
        """
        print(u'在 %s-%s 上传 %s' % (page['menu'], page['page'], value))
        xpath = self.get_ele_xpath(page['menu'], page['page'], key)
        if 'input' not in xpath:
            xpath = '//input[@type="file"]'
        ele = self._find_ele(xpath)
        for i in range(1, 10):
            try:
                ele.send_keys(value)
                self.screenshot(log_level='info')
                print(u'操作成功，等待上传完成')
                return True
            except InvalidElementStateException:
                self.screenshot(log_level='warn')
                sleep(1)
        self.screenshot(log_level='error')
        raise InvalidElementStateException

    def refresh_page(self):
        """
        刷新页面
        :return:
        """
        self.browser.refresh()


if __name__ == '__main__':
    print('This is common/Browser')
