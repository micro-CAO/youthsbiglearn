##该程序由hugefunny倾力打造，授权给telegram @L14_514开源。有任何问题，请提交issues。
##如果你对其中的原理感兴趣，你可以发信给ckfu20219@gmail.com或电报联系@L14_514交流。
##双井号是开源者添加的注释，单井号是hugefunny加的注释

from selenium import webdriver ##注意：必须安装selenium模块！详情请浏览代码底部的注释
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#导入浏览器自动化模块以及辅助模块

browser = webdriver.Edge()
browser.get('http://qndxx.bestcood.com/nanning/daxuexi/')
##要操作的网址，作者以南宁青年大学习编写。其他地区的大学习可能需要变更按钮id等

NameList = ['真白花音','李田所','卢本伟']
#姓名列表

IDList = ['233333','114514','1721729']
#ID列表

mount = 0
#初始化数值

while mount < 3:
    #学生数量

    userName = browser.find_element(By.ID,'userName')
    userName.send_keys(NameList[int(mount)])
    #输入姓名

    userId = browser.find_element(By.ID,'userId')
    userId.send_keys(IDList[int(mount)])
    #输入ID

    login = browser.find_element(By.ID,'btn-login')
    login.send_keys(Keys.ENTER)
    #登陆确认

    time.sleep(2)
    learnstart = browser.find_element(By.XPATH,'//*[@id="btn-learn-start"]')
    learnstart.click()
    #开始学习

    time.sleep(1)
    browser.back()
    #返回上一级

    exit = browser.find_element(By.CLASS_NAME,'sign-out')
    exit.click()
    #退出登录

    mount = mount + 1
    #循环往复

#在填写名单的时候请注意ID和名字要顺序对应
#即名字列表里的填写第一个名字对应第一个填写的ID
#第二个填写名字对应填写的第二个ID，以此类推
#有更多同学就添加更多单引号和逗号，依旧要记得按次序对应

#使用本脚本需要安装前置模块selenium
#请转到python的安装目录，在顶部导航栏输入powershell,回车
#在对话框输入pip install selenium
#如果显示不知道pip是什么一类的响应，请安装或者重新安装python于设备

#浏览器需要安装对应的webdriver模块
#推荐使用Firefox浏览器，selenium的默认浏览器就是Firefox，当然新版Microsoft edge也是不错的选择！
#浏览器访问https://github.com/mozilla/geckodriver/releases
#点击第一个有红色椭圆框包围的Latest按钮
#滚动到网站底部的Assets，点击geckodriver-v[数字].[数字].[数字]-win64/32.zip
#请检查你的Firefox版本是32位还是64位，32位安装win32，64位安装win64
#别问我怎么检查，一般都是64位，不会检查就安装64位
#下载的压缩包解压出来的文件，放到和python安装目录
#没有意外应该就可以运行了

#目前测试没有bug，有问题还请hugefunny@hotmail.com或ung225625@outlook.com或ckfu20219@gmail.com
