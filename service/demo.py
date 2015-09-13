#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Author: Dong Guo
# Last modified: 2015-03-11 02:47 UTC

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
        with lcd(settings.PROJECT_HOME):
            put('data/demo/demo_upload.txt','/tmp/') 

    def deploy(self):
        print(green("Deploy action"))
        cmds = ['cp -a /tmp/demo_deploy.txt /tmp/demo_deploy.txt.prev',
                'mv -f /tmp/demo_upload.txt /tmp/demo_deploy.txt']
        sudo(' && '.join(cmds))

    def rollback(self):
        print(green("Rollback action"))
        sudo('mv -f /tmp/demo_deploy.txt.prev /tmp/demo_deploy.txt')
