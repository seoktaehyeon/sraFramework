*** Settings ***
Documentation       about Api keywords
Library             ../pages/qsphere/Welcome.py
Library             ../pages/about/Api.py


*** Keywords ***
SRAF.about.Api.进入页面
    access api page

SRAF.about.Api.检查标题
    check api page title

SRAF.about.Api.输入Swagger文件
    [Arguments]         ${file_path}
    input swagger json path         ${file_path}

SRAF.about.Api.点击SwaggerExplore按钮
    click explore button
