*** Settings ***
Documentation       This is Demo for SRAF
Resource            ../keywords/qsphereWelcome.robot
Resource            ../keywords/qsphereVision.robot
Resource            ../keywords/aboutApi.robot
Resource            ../keywords/extAllure.robot
Resource            ../keywords/extOpendevops.robot
Test Setup          SRAF.开始测试
Test Teardown       SRAF.结束测试


*** Variables ***
SwaggerJson         /objects/openapi-v1.json


*** Test Cases ***
SRAF 应用的演示
    [Documentation]     在目标网页上进行一些点击操作
    [Tags]              Demo
    SRAF.qsphere.Vision.进入页面
    SRAF.qsphere.Vision.检查标题
    SRAF.about.Api.进入页面
    SRAF.about.Api.检查标题
    SRAF.about.Api.输入Swagger文件      $SwaggerJson
    SRAF.about.Api.点击SwaggerExplore按钮
    SRAF.ext.Allure.进入页面
    SRAF.ext.Allure.检查标题
    SRAF.ext.Allure.点击菜单            安装
    SRAF.ext.Opendevops.接入页面
    SRAF.ext.Opendevops.检查标题


*** Keywords ***