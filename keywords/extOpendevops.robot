*** Settings ***
Documentation       ext OpenDevOps keywords
Library             ../pages/ext/Opendevops.py


*** Keywords ***
SRAF.ext.Opendevops.进入页面
    access odo page

SRAF.ext.Opendevops.检查标题
    check odo title
