#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from common.Browser import Browser
from common import elePages


os.environ['RF_PWD'] = os.path.join('.')
os.environ['RF_DIR'] = os.path.join('.')
os.environ['RF_VAR_FILE'] = os.path.join('.', 'config', 'demo.yaml')
assert os.path.exists(os.getenv('RF_VAR_FILE')), u'文件不存在'

browser = Browser()
browser.access(url='https://qualitysphere.gitee.io')
browser.click_button(
    page=elePages.qsphere.Vision(),
    key=u'愿景'
)
browser.close_chrome()
