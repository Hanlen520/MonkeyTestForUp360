# -*- coding: utf-8 -*-
import time,os
from BLL import BAdbCommon
from Common import OperateFile
from BLL import BMonkeyConfig
from Model import MMonkeyConfig

if __name__ == '__main__':
    ini_file = 'monkey.ini'
    ba = BAdbCommon
    if OperateFile.base_file(ini_file, "r").check_file():
        if ba.attached_devices():
            mconfig = MMonkeyConfig.monkeyconfig()
            mc = BMonkeyConfig.monkeyConfig(mconfig, ini_file, 'Teacher', 1000)

            print(mc.apk_dir)

            for files in os.listdir(mc.apk_dir):
                if 'teacher' in files:
                    mc.package_name = 'com.up360.teacher.android.activity'
                elif 'parents' in files:
                    mc.package_name = 'com.up360.parents.android.activity'
                print(files)
                ba.uninstall_app(mc.package_name)
                time.sleep(2)
                ba.install_app(mc.apk_dir+"\\"+files, files)
                time.sleep(2)

                if 'teacher' in files:
                    mc.package_name = 'com.up360.teacher.android.activity'
                elif 'parents' in files:
                    mc.package_name = 'com.up360.parents.android.activity'
                else:
                    mc.package_name = mc.simiasque_package_name
                    mc.activity = mc.simiasque_package_activity

                ba.open_app(mc.package_name, mc.activity)

        else:
            print("设备不存在")
    else:
        print(u"配置文件不存在"+ini_file)



