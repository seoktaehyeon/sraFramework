*** Settings ***
Documentation       qsphere Vision keywords
Library             ../pages/qsphere/Vision.py


*** Keywords ***
SRAF.qsphere.Vision.进入页面
    access vision page

SRAF.qsphere.Vision.检查标题
    check vision page title
