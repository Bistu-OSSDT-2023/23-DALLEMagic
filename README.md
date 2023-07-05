# DALL·E Magic

### 开发人员：

[郑嘉鑫](https://github.com/xhfandm)：主要参与编写课程答辩PPT，项目方向设定，参加课程答辩等

[张博宣](https://github.com/zbxxbz)：主要参与编写Main.py，同时参与openai_module.py的编写等

[郑嘉杰](https://github.com/zhengjiajie2)：主要参与编写项目文档，开源项目api文档查阅等

[杜凌羽](https://github.com/githubzuoye)：主要参与编写课程项目建设发布报告，参与编写tencent_module.py的编写等

[门奕锟](https://github.com/jokermxm)：主要参加编写项目文档、课程项目建设发布报告的编写，挑选开源协议等



### 项目结构：

openai_module.py：主要用于调用OpenAI官方的API，我们主要参考了[OpenAI官方API文档](https://platform.openai.com/docs/api-reference)

tecent_module.py：主要用于调用Tencent官方的人像动漫化API，我们主要参考了[Tencent官方API文档](https://cloud.tencent.com/document/product/1202/41967)

Main.py:主要使用tkinter库创建了一个图形用户界面应用程序窗口，接入Tencent和OpenAI的API，实现了

生成图像、放大图像、保存图像、卡通画图像这四个功能



### 使用方法:

#### 方法一：本地编译

1. 将项目导入**Pycharm**

2. 使用**pip install openai**，**pip install tkinter**等所需的Python包

3. 运行**Main.py**即可

#### 方法二：使用预编译好的exe文件

我们已经使用Auto Py To Exe将程序打包成.exe可执行文件，实现了在Windows系统中下载即用，相关文件在项目**Pre compiler**目录下。



### 注意事项：

#### 1.网络环境

OpenAI的API禁止国内访问，在生成图片时需要挂非亚洲代理，国内请求API会导致封号

#### 2.使用问题

生成图片数目为必填项，没有填写生成图片数目会导致程序崩溃

不要重复点击生成按钮，这样也会导致程序的崩溃



### 许可证：

该项目采用 [Apache 2.0 许可证](https://www.apache.org/licenses/LICENSE-2.0) 进行许可。
