*** Settings ***
Documentation       ext Allure keywords
Library             ../pages/ext/Allure.py


*** Keywords ***
SRAF.ext.Allure.进入页面
    access allure page

SRAF.ext.Allure.检查标题
    check allure page title

SRAF.ext.Allure.点击菜单
    [Arguments]         ${menu}
    click menu          ${menu}
