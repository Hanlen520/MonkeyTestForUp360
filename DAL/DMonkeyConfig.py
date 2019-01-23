__author__ = 'Administrator'
import configparser
import time
def monkeyConfig(mmonkeyconfig, init_file, Apply, sum):
    config = configparser.ConfigParser()
    config.read(init_file)
    mmonkeyconfig.package_name = config[Apply]['package_name']
    mmonkeyconfig.logdir = config[Apply]['logdir']
    mmonkeyconfig.now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    mmonkeyconfig.activity = config[Apply]['activity']
    mmonkeyconfig.sum = int(config[Apply]['sum'])
    mmonkeyconfig.monkey_log = mmonkeyconfig.logdir + "\\" + mmonkeyconfig.now + "\\" + mmonkeyconfig.now + "_" + Apply + r"_monkey.log"
    mmonkeyconfig.cmd = config[Apply]['cmd'] + " " + str(sum) + ">>" + mmonkeyconfig.monkey_log
    mmonkeyconfig.phone_msg_log = mmonkeyconfig.logdir + "\\" + mmonkeyconfig.now + "\\"
    mmonkeyconfig.tools_dir = config[Apply]['tools_dir']
    mmonkeyconfig.apk_dir = config[Apply]['apk_dir']
    mmonkeyconfig.simiasque_apk_name = config[Apply]['simiasque_apk_name']
    mmonkeyconfig.simiasque_package_name = config[Apply]['simiasque_package_name']
    mmonkeyconfig.simiasque_package_activity = config[Apply]['simiasque_package_activity']
    return mmonkeyconfig