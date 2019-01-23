from DAL.DAdbCommon import *


# 检查设备是否存在
def attached_devices():
    return AndroidDebugBridge().attached_devices()

# 打开APP
def open_app(package_name, activity):
    return AndroidDebugBridge().open_app(package_name, activity)

# 关闭APP
def close_app(package_name):
    return AndroidDebugBridge().close_app(package_name)

# 安装APP
def install_app(install_apk, apk_name):
    return AndroidDebugBridge().install_app(install_apk, apk_name)

# 安装APP
def uninstall_app(package_name):
    return AndroidDebugBridge().uninstall_app(package_name)

# 执行命令
def exec_command(command):
    return AndroidDebugBridge().call_adb(command)

# 关闭进程
def close_app_id(package_name):
    return AndroidDebugBridge().close_app_pid(package_name)

# 截图
def get_screenshot(computer_dir, image_name, mobile_dir="/data/local/tmp/"):
    return AndroidDebugBridge().get_screenshot(computer_dir, image_name, mobile_dir)
