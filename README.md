# monkey 压力测试android 
## Monkey的特征
* 测试的对象仅为应用程序包，有一定的局限性。
* Monkey测试使用的事件流数据流是随机的，不能进行自定义。
* 可对MonkeyTest的对象，事件数量，类型，频率等进行设置。
 
## Monkey的基本用法
* 基本语法如下：
	* $ adb shell monkey [options]
	* 如果不指定options，Monkey将以无反馈模式启动，并把事件任意发送到安装在目标环境中的全部包。下面是一个更为典型的命令行示例，它启动指定的应用程序，并向其发送500个伪随机事件：
	* $ adb shell monkey -p your.package.name -v 500
## 分析日志
* 通过Android trace文件分析死锁ANR实例过程
* system/build.prop 日志文件主要记录手机系统信息，如版本，型号，品牌
* adb logcat 导出日志文件


schematics




