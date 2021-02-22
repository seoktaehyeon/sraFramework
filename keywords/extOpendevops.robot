*** Settings ***
Documentation       ext OpenDevOps keywords
Library             ../pages/ext/Opendevops.py


*** Keywords ***
SRAF.ext.Opendevops.进入页面
    access opendevops page

SRAF.ext.Oepndevops.检查标题
    check opendevops page title
