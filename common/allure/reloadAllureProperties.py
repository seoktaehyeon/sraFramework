#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import yaml
import platform


def allure_cmd_exist():
    if os.getenv('ALLURE_CMD') != "true":
        print(u'由于没有 Allure Command Line，因此不生成 Allure Report')
        exit(0)


if __name__ == '__main__':
    allure_cmd_exist()
    if os.getenv('RF_PWD') and os.getenv('RF_VAR_FILE'):
        with open(os.path.join(os.getenv('RF_PWD'), 'output', 'browser.json'), 'r', encoding='utf-8') as f:
            bs_info = json.loads(f.read())
        allure_properties_template_dir = os.path.join(os.getenv('RF_PWD'), 'common', 'allure')
        allure_results_dir = os.path.join(os.getenv('RF_PWD'), 'output', 'allure-results')
        with open(os.getenv('RF_VAR_FILE'), 'r', encoding='utf-8') as f:
            allure_test_url = yaml.full_load(f.read()).get('TARGET_URL')
    else:
        bs_info = None
        allure_properties_template_dir = '.'
        allure_results_dir = os.path.join('..', '..', 'output', 'allure-results')
        with open(os.path.join('..', '..', 'config', 'template.yaml'), 'r', encoding='utf-8') as f:
            allure_test_url = yaml.full_load(f.read()).get('TARGET_URL')
    # 格式化环境信息
    allure_env_xml_tmpl_file = os.path.join(allure_properties_template_dir, 'environment.xml')
    allure_categories_tmpl_file = os.path.join(allure_properties_template_dir, 'categories.json')
    allure_executor_tmpl_file = os.path.join(allure_properties_template_dir, 'executor.json')
    allure_exec_framework = 'RobotFramework'
    allure_exec_browser_name = bs_info['browserName'] if bs_info else 'Unknown'
    allure_exec_browser_ver = bs_info['browserVersion'] if bs_info else 'Unknown'
    allure_exec_sys_name = platform.system()
    allure_exec_sys_ver = platform.version()
    allure_exec_py_ver = platform.python_version()
    """Allure 环境信息"""
    with open(allure_env_xml_tmpl_file, 'r', encoding='utf-8') as f:
        allure_env_xml = f.read()
    allure_env_xml = allure_env_xml.replace('ALLURE_TEST_URL', allure_test_url)
    allure_env_xml = allure_env_xml.replace('ALLURE_EXEC_FRAMEWORK', allure_exec_framework)
    allure_env_xml = allure_env_xml.replace('ALLURE_EXEC_BROWSER_NAME', allure_exec_browser_name)
    allure_env_xml = allure_env_xml.replace('ALLURE_EXEC_BROWSER_VER', allure_exec_browser_ver)
    allure_env_xml = allure_env_xml.replace('ALLURE_EXEC_SYS_NAME', allure_exec_sys_name)
    allure_env_xml = allure_env_xml.replace('ALLURE_EXEC_SYS_VER', allure_exec_sys_ver)
    allure_env_xml = allure_env_xml.replace('ALLURE_EXEC_PY_VER', allure_exec_py_ver)
    """Allure 运行器信息"""
    with open(allure_categories_tmpl_file, 'r', encoding='utf-8') as f:
        allure_categories_json = json.loads(f.read())
    """Allure 类别信息"""
    with open(allure_executor_tmpl_file, 'r', encoding='utf-8') as f:
        allure_executor_json = json.loads(f.read())
    """生成当前 Allure 配置文件"""
    with open(os.path.join(allure_results_dir, 'environment.xml'), 'w', encoding='utf-8') as f:
        f.write(allure_env_xml)
    with open(os.path.join(allure_results_dir, 'categories.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(allure_categories_json))
    with open(os.path.join(allure_results_dir, 'executor.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(allure_executor_json))
