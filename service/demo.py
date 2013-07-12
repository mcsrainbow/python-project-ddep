#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: demo.py
# Date: Fri 29 Mar 2013 04:51:25 AM CST
# Author: Dong Guo

from fabric.api import *
from fabric.colors import *
from service import global_settings

settings = global_settings

class FabricSupport(object):
    def __init__(self):
        pass

    def execute(self,task,hosts,number,user,keyfile):
        env.parallel = True
        env.pool_size = number
        env.user = user
        env.key_filename = keyfile

        get_task = "task = self.{0}".format(task)
        exec get_task

        execute(task,hosts=hosts)

    def upload(self):
        print(green("Transfer the file demo_upload.txt"))
        with lcd (settings.PROJECT_HOME):
            put('data/demo/demo_upload.txt','/tmp/') 

    def deploy(self):
        print(green("Deploy action"))
        cmds = [
                'mv -f /tmp/demo_upload.txt /home/adsymp/jetty/webapps/demo_upload.txt.YYYYMMDD',
                'mv -f /home/adsymp/jetty/webapps/demo_upload.txt /home/adsymp/jetty/webapps/demo_upload.txt.prev',
                'cp -a /home/adsymp/jetty/webapps/demo_upload.txt.YYYYMMDD /home/adsymp/jetty/webapps/demo_upload.txt',
               ]
        sudo(' && '.join(cmds))

    def rollback(self):
        print(green("Rollback action"))
        sudo('mv -f /home/adsymp/jetty/webapps/demo_upload.txt.prev /home/adsymp/jetty/webapps/demo_upload.txt')
