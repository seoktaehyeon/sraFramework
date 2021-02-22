#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: v.stone@163.com
"""
common
+-- elePages
    +-- __init__.py
    +-- menu_name.py

__init__.py
from . import menu_name

menu_name.py
def Page_Name():
    return {
        'menu': '',
        'page': '',
    }
"""

import os


def generate_menu_cls():
    print('Extract elements dir to generate menu class ... ', end='\t')
    ele_menu_list = list()
    ele_menu_dir = os.path.join(os.getenv('RF_PWD'), 'pages')
    for _dir in os.listdir(ele_menu_dir):
        if os.path.isdir(os.path.join(ele_menu_dir, _dir)):
            ele_menu_list.append(_dir)
    print('DONE')
    # print(ele_menu_list)
    ele_pages_dir = os.path.join(os.getenv('RF_PWD'), 'common', 'elePages')
    ele_pages_init = os.path.join(os.getenv('RF_PWD'), 'common', 'elePages', '__init__.py')
    # print(ele_pages_init)
    if not os.path.exists(ele_pages_dir):
        os.mkdir(ele_pages_dir)
    ele_cls = [
        '#!/usr/bin/env python3',
        '# -*- coding: utf-8- -*-',
        '# Author: elementGenerator.py',
        '\n'
    ]
    for ele_menu in ele_menu_list:
        ele_cls.append('from . import %s' % ele_menu)
    with open(ele_pages_init, 'w') as f:
        f.write('\n'.join(ele_cls))
    # with open(ele_pages_init, 'r') as f:
    #     print(f.read())
    return ele_menu_list


def generate_page_py(ele_menu: str):
    print('Extract menu %s dir to generate page py ... ' % ele_menu, end='\t')
    ele_page_py = os.path.join(
        os.getenv('RF_PWD'),
        'common',
        'elePages',
        '%s.py' % ele_menu
    )
    ele_def = [
        '#!/usr/bin/env python3',
        '# -*- coding: utf-8- -*-',
        '# Author: elementGenerator.py',
        '\n'
    ]
    ele_page_dir = os.path.join(os.getenv('RF_PWD'), 'pages', ele_menu)
    for ele_page in os.listdir(ele_page_dir):
        if not ele_page.startswith('__'):
            ele_def.append('\n'.join([
                'def %s():' % ele_page.split('.py')[0],
                '\treturn {',
                '\t\t"menu": "%s",' % ele_menu,
                '\t\t"page": "%s",' % ele_page.split('.py')[0],
                '\t}',
                '\n'
            ]))
    print('DONE')
    with open(ele_page_py, 'w') as f:
        f.write('\n'.join(ele_def))
    # with open(ele_page_py, 'r') as f:
    #     print(f.read())
    return True


if __name__ == '__main__':
    for menu_name in generate_menu_cls():
        generate_page_py(menu_name)
