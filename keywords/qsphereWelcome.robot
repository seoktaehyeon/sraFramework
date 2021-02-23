*** Settings ***
Documentation       qsphere Welcome keywords
Library             ../pages/qsphere/Welcome.py


*** Keywords ***
SRAF.开始测试
    access homepage         ${TARGET_URL}
    check page title        ${TARGET_TITLE}

SRAF.结束测试
    close browser

SRAF.访问主页
    SRAF.开始测试
