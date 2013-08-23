#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: config.py
# Date: Fri 29 Mar 2013 07:26:50 AM CST
# Author: Dong Guo

import os
import ConfigParser

# get the settings from service/global_settings.py
from service import global_settings

config = ConfigParser.ConfigParser()
settings = global_settings

def dbconf():
    """Get the database values from conf/db.ini."""

    try:
        file = os.path.join(settings.CONFIG_HOME, 'db.ini')
        config.read(file)
        host = config.get("default", "host")
        database = config.get("default", "database")
        user = config.get("default", "user")
        password = config.get("default", "password")
    except ConfigParser.Error, e:
        print '{0}'.format(e)
        return False
    else:
        return {'host':host,'database':database,'user':user,'password':password}

def userconf():
    """Get the username and keyfile path from conf.auth.ini."""

    try:
        file = os.path.join(settings.CONFIG_HOME, 'auth.ini')
        config.read(file)
        user = config.get("default", "user")
        keyfile = settings.PROJECT_HOME + "/data/keyfiles/" + config.get("default", "keyfile")
    except ConfigParser.Error, e:
        print '{0}'.format(e)
        return False
    else:
        return {'user':user, 'keyfile':keyfile}
