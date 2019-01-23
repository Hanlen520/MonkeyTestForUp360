from BLL import BAdbCommon
import sys


# 停止脚本测试
def stop_monkey():
    ba = BAdbCommon
    ba.close_app_id("monkey")

if __name__ == '__main__':
    stop_monkey()


