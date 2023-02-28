# 青年大学习自动化程序

当今的中国，在党的领导下走上了现代化道路！为了更好培养青年的先进思想，我们党利用了互联网传播“**青年大学习**”课程。

可是，在一些场景，我们手头拿不到手机（比如中学内宿生），如果要完成上级要求的大学习任务，就不得不用公用计算机来完成。因此，可能会出现教室希沃one by one打姓名、学习号的情况，甚至需要单独给某个同学查找学习号......这多浪费时间！

因此，我和 @hugefunny 共同利用python，写了这款程序！

点击“**released**”，即可获取python程序。使用前请右键使用文本编辑器（推荐visual studio code）浏览源码及其注释


# 使用说明
在填写名单的时候请注意ID和名字要顺序对应
即名字列表里的填写第一个名字对应第一个填写的ID
第二个填写名字对应填写的第二个ID，以此类推
有更多同学就添加更多单引号和逗号，依旧要记得按次序对应

使用本脚本需要安装前置模块selenium
请转到python的安装目录，在顶部导航栏输入powershell,回车
在对话框输入pip install selenium
如果显示不知道pip是什么一类的响应，请安装或者重新安装python于设备

浏览器需要安装对应的webdriver模块
推荐使用Firefox浏览器，selenium的默认浏览器就是Firefox，当然新版Microsoft edge也是不错的选择！
浏览器访问https://github.com/mozilla/geckodriver/releases
点击第一个有红色椭圆框包围的Latest按钮
滚动到网站底部的Assets，点击geckodriver-v[数字].[数字].[数字]-win64/32.zip
请检查你的Firefox版本是32位还是64位，32位安装win32，64位安装win64
别问我怎么检查，一般都是64位，不会检查就安装64位
下载的压缩包解压出来的文件，放到和python安装目录
没有意外应该就可以运行了

目前测试没有bug，有问题还请hugefunny@hotmail.com或ung225625@outlook.com或ckfu20219@gmail.com
# 提示
我们的程序只能直接用于南宁市的青年大学习网站！你可以提交issue让我们适配其他地区的青年大学习。
