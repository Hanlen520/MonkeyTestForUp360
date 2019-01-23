# -*- coding: utf-8 -*-
import os
import time
import sys
from BLL import BAdbCommon
from Common import OperateFile
from BLL import BMonkeyConfig
from Model import MMonkeyConfig
import re
from Common import Globals as go
from BLL import BphomeMsg
from Common import Cprint

def get_error(log, dir, file_name):
    ba = BAdbCommon
    cp = Cprint.Color() # 在cmd中输出带颜色的命名
    anr_log = OperateFile.base_file(dir+"\\"+file_name+"_anr.log", "a+")
    crash_log = OperateFile.base_file(dir + "\\"+file_name+"_crash.log", "a+")
    exception_log = OperateFile.base_file(dir + "\\"+file_name+"_exception.log", "a+")

    with open(log, encoding="utf-8") as monkey_log:
        lines = monkey_log.readlines()
        for line in lines:
            if re.findall(go.ANR, line):
                # print('\033[1;31;42m')
                # print("存在anr错误:", line)
                cp.print_red_text("存在anr错误:" + line)
                anr_log.write_txt(str(go.I_ANR)+":"+line)
                go.I_ANR += 1

            if re.findall(go.CRASH, line):
                # print('\033[1;31;42m')
                cp.print_red_text("存在crash错误:"+line)
                crash_log.write_txt(str(go.I_CRASH)+":"+line)
                go.I_CRASH += 1

            if re.findall(go.EXCEPTION, line):
                # print('\033[1;31;42m')
                cp.print_red_text("存在exception异常:"+line)
                exception_log.write_txt(str(go.I_EXCEPTION)+":"+line)
                go.I_EXCEPTION += 1

        if go.I_ANR == 0 and go.I_CRASH == 0 and go.I_EXCEPTION == 0:
            cp.print_green_text("恭喜，没有任何错误")

 # 存手机信息
def get_phone(phonelog):
    bg = BphomeMsg.getPhone("log.txt").get_phone_Kernel()
    logname = phonelog + "_" + bg[0]["phone_model"] + bg[0]["phone_name"] + bg[0]["release"] + ".txt"
    of = OperateFile.base_file(logname, "w+")
    if of.create_file():
        result = "手机型号：" + bg[0]["phone_name"] + "\n"
        result += "手机名字：" + bg[0]["phone_model"] + "\n"
        result += "系统版本：" + bg[0]["release"] + "\n"
        result += "手机分辨率：" + bg[3] + "\n"
        result += "手机运行内存：" + bg[1] + "\n"
        result += "CPU核数：" + bg[2] + "\n"
        of.write_txt(result)

# 开始脚本测试
def start_monkey(cmd, logdir, now1, apply):
    # 判断目录是否存在
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    # Monkey测试结果日志:monkey_log
    os.popen(cmd)
    print(cmd)
    os.mkdir(logdir+"\\"+now1) #创建日志目录

    # Monkey时手机日志logcat
    logcatname = logdir+"\\"+now1+"\\"+now1 + "_" + apply + r"_logcat.log"
    cmd2 = "adb logcat -d >%s" %(logcatname)
    os.popen(cmd2)

def run_monkey():
    ini_file = 'monkey.ini'
    apply_type = sys.argv[1]
    sum_config = sys.argv[2]

    if apply_type == 'T':
        apply = 'Teacher'
    elif apply_type == 'P':
        apply = 'Parents'
    else:
        apply = 'Teacher'

    ba = BAdbCommon
    if OperateFile.base_file(ini_file, "r").check_file():
        if ba.attached_devices():
            mconfig = MMonkeyConfig.monkeyconfig()
            mc = BMonkeyConfig.monkeyConfig(mconfig, ini_file, apply, sum_config)

            # 1.安装并打开设置屏蔽下拉框工具
            if not ba.open_app(mc.simiasque_package_name, mc.simiasque_package_activity):
                time.sleep(2)
                ba.install_app(mc.tools_dir+"\\"+mc.simiasque_apk_name, mc.simiasque_apk_name)
                time.sleep(5)
                ba.open_app(mc.simiasque_package_name, mc.simiasque_package_activity)

            time.sleep(2)
            ba.exec_command("shell am broadcast -a org.thisisafactory.simiasque.SET_OVERLAY --ez enable true")
            time.sleep(1)

            log_dir = mc.logdir+"\\"+mc.now
            # 打开测试APP
            if ba.open_app(mc.package_name, mc.activity):
                temp = ""
                # monkey开始测试
                start_monkey(mc.cmd, mc.logdir, mc.now, apply)
                while True:
                    with open(mc.monkey_log, encoding='utf-8') as monkeylog:
                        if monkeylog.read().count('Monkey finished') > 0:
                            print("测试完成咯")
                            get_error(mc.monkey_log, mc.logdir+"\\"+mc.now, mc.now+"_"+apply)
                            get_phone(mc.phone_msg_log)
                            break

                # 关闭 测试APP和屏蔽下拉框APP
                ba.close_app(mc.package_name)
                ba.exec_command("shell am broadcast -a org.thisisafactory.simiasque.SET_OVERLAY --ez enable false")
                ba.close_app(mc.simiasque_package_name)
            else:
                print("被测应用未安装!")
        else:
            print("设备不存在!")
    else:
        print(u"配置文件不存在"+ini_file)
    return os.path.abspath('.') + mc.logdir+"\\"+mc.now


if __name__ == '__main__':
    print("<a href='" + run_monkey()+"_Teacher_monkey.log" + "'>111</a>")

