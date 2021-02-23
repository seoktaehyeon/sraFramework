# sraFramework
The solution of Selenium + RobotFramework + Allure Reporting Tool

> 一套用以 Web 界面端到端测试的自动化解决方案

## 环境准备

- Chrome + Webdriver <br> [Webdriver 列表](http://npm.taobao.org/mirrors/chromedriver/)
- Bash
- Python3
- Python 依赖包 <br> `pip install -r requirements.txt`
- RobotFramework
- JRE + Allure Commandline (可选) <br> [Allure 安装方法](https://qualitysphere.gitee.io/4_allure/#21-安装)
- Docker (可选)

## 目录结构

目录|作用|文件命名|文件内容示例
----|----|----|----
testcase|用于存放测试用例|\<suite\>.robot|[testcase/demo.robot](testcase/demo.robot)
keywords|用于存放关键字<br>*以便在编写 testcase 中的用例时引用*|\<menu\>\<Page\>.robot|[keywords/qsphereVision.robot](keywords/qsphereVision.robot)
pages|用于存放封装好的页面元素操作函数<br>*以便在封装 keywords 中的关键字时使用*|\<menu\>/\<Page\>.py|[pages/qsphere/Vision.py](pages/qsphere/Vision.py)
elements|用于存放页面元素的 xpath<br>*以便被 pages 中的函数加载*|\<menu\>/\<Page\>.yaml|[elements/qsphere/Vision.yaml](elements/qsphere/Vision.yaml)
common|用于存放与产品解耦的基础函数<br>*以便被 pages 中的函数调用*|xxx.py|[common/Browser.py](common/Browser.py)
config|用于存放用例执行过程中使用的全局变量和测试数据<br>*以便在 testcase 或 keywords 中可以直接引用*|xxx.yaml|[config/template.yaml](config/template.yaml)

## 如何使用

#### 准备配置文件

- 复制模板

```bash
cp config/template.yaml config/demo.yaml
```

- 修改 demo.yaml 配置中的变量值

```yaml
# RobotFramework Configuration
# If you wanna debug via browser, you can set RF_DEBUG as true
RF_DEBUG: false

# Target Configuration
TARGET_URL: https://qualitysphere.gitee.io
TARGET_USER: will
TARGET_PASSWORD: password
TARGET_TITLE: 欢迎使用 | QSphere
```
#### 执行测试用例

- --config 指定配置文件执行测试用例

```bash
./sraf-cmd --config config/demo.yaml --clean
```

- --tag 执行指定标签的测试用例

```bash
./sraf-cmd --config config/demo.yaml --tag demo --clean
```

- --suite 执行指定测试集中的测试用例

```bash
./sraf-cmd --config config/demo.yaml --suite testcase/demo.robot --clean
```

> 更多用法请运行 `./sraf-cmd` 查看

#### 如何本地调试

```python
import os
from common.Browser import Browser
from common import elePages


os.environ['RF_PWD'] = os.path.join('.')
os.environ['RF_DIR'] = os.path.join('.')
os.environ['RF_VAR_FILE'] = os.path.join('.', 'config', 'template.yaml')
assert os.path.exists(os.getenv('RF_VAR_FILE')), u'文件不存在'

browser = Browser()
browser.access(url='https://qualitysphere.gitee.io')
browser.click_button(
    page=elePages.qsphere.Vision(),
    key=u'愿景'
)
browser.close_chrome()
```

#### 如何在容器中执行

```bash
docker build --pull -t sraf-cmd:local .
docker run --shm-size=1g --rm -p 80:80 -it sraf-cmd:local bash -c "./sraf-cmd --config config/demo.yaml --tag demo --clean --report local-allure"
# 若在 windows 中执行，需要在命令前面使用 winpty
winpty docker run --shm-size=1g --rm -p 80:80 -it sraf-cmd:local bash -c "./sraf-cmd --config config/demo.yaml --tag demo --clean --report local-allure"
```

## 编写测试用例

#### 在 testcase 目录中编写测试用例

`testcase/test_case.robot`
```robotframework
*** Settings ***
Documentation       用例集描述
Resource            ../keywords/<menu><Page>.robot     # 引入关键字资源
Test Setup          SRAF.开始测试
Test Teardown       SRAF.结束测试

*** Variables ***

*** Test Cases ***
SRAF 测试用例标题
    [Documentation]     用例描述
    [Tags]              标签1    标签2
    SRAF.menu1.Page1.关键字1
    SRAF.menu1.Page1.关键字2

*** Keywords ***

```
#### 在 keywords 目录中封装关键字

`keywords/<menu><Page>.robot`
```robotframework
*** Settings ***
Documentation    关键字说明
Library    ../pages/<menu>/<Page>.py        # 导入封装的 py 包

*** Keywords ***
SRAF.<menu>.<Page>.关键字
    <python_def>    ${KDP_VAR_1}    ${KDP_VAR_1}

```

#### 在 pages 目录中按照页面元素封装功能

`pages/<menu>/<Page>.py`
```python
from common.Browser import Browser
from common import elePages


class PageName(object):
    def __init__(self):
        self.browser = Browser()

    def login_kdp(self, user: str, password: str):
        self.browser.input_text(
            page=elePages.menu1.Page1(),
            key=u'登录名',
            value=user
        )
        self.browser.input_text(
            page=elePages.menu1.Page1(),
            key=u'密码',
            value=password
        )
        self.browser.click_button(
            page=elePages.menu1.Page1(),
            key=u'登录'
        )

    def upload_file(self):
        self.browser.upload_file(
            page=elePages.menu2.Page4(),
            key=u'上传附件',
            value='/workspace/demo_attach.png'
        )
```

#### 在 elements 目录中存储页面元素的 xpath

`elements/<menu>/<Page>.yaml`
```yaml
元素名称: 'xpath'
```
