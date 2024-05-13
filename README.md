# “江苏图采”微信小程序照片上传工具


主要原理：Charles抓包，Map Remote到本地Flask服务器，使用Multipart Encoder修改multipart中的照片文件。

目前还未实现wx.login()的code自动获取。欢迎大佬提PR共同完善此项目！🫡



## 小程序源码解析+简单的手动上传方案
https://blog.csdn.net/qq_27683537/article/details/138774682



## 操作步骤
### 1.配置Charles抓包
现在安卓系统越来越封闭，建议使用IOS/PC/MAC端配置好Charles抓包（Fiddler等工具也可以）。具体方法自行搜索，这里不再赘述。

配置好后，请先在小程序中跑一遍上传逻辑，确认可以正常抓到“jstxcj.91job.org.cn”的包

### 2.修改并运行modify_multipart.py
请将程序中第40行的照片路径修改为你要上传的照片路径，然后运行：
```bash
pip3 install flask
python3 /path/to/modify_multipart.py
```

### 3.Charles中配置好Map Remote
具体配置流程可参考csdn博客。注意端口号和程序中保持一致，如果运行在本机，Map To的Host就填127.0.0.1。参考配置如下：

<img width="60%" alt="截屏2024-05-13 23 43 25" src="https://github.com/Little-King2022/jstc_pic_uploader/assets/110970384/6b8841ca-edee-4760-99ef-87059a6e1c4b">

### 4.在小程序中直接拍照吧～
你会惊讶地发现，照片会被成功替换！🥳

如果没有，控制台中将输出详细的错误信息，供你参考。如需帮助，请参考csdn博客，或在此提交Issue。


