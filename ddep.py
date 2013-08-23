#!/usr/bin/env python
#-*- coding:utf-8 -*-

# FileName: fabfile.py
# Date: Thu 28 Mar 2013 10:21:18 PM CST
# Author: Dong Guo

import sys
import os

# torndb is a lightweight wrapper around MySQLdb
from utils.torndb import Connection

# configuration files from conf/db.ini and conf/auth.ini
from service.config import dbconf, userconf

def parse_opts():
    """Help messages (-h, --help) for ddep.py"""
    
    # import the libraries
    import textwrap
    import argparse

    # the user-defined description
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
        '''
        examples:
          ./ddep.py -H web1,web2,web3 -p demo -t upload
          ./ddep.py -g webserver -p demo -t upload
          ./ddep.py -g webserver -p demo -t upload -z 2
        '''
        ))
    
    exclusion = parser.add_mutually_exclusive_group()

    # set the arguments
    exclusion.add_argument('-g', metavar='group', type=str,
            help='all hosts of the group')
    exclusion.add_argument('-H', metavar='hosts', type=str,
            help='comma-separated list of hosts to operate on')
    parser.add_argument('-p', metavar='project', type=str, required=True,
            help='plugged-in project')
    parser.add_argument('-t', metavar='task', type=str, required=True,
            help='task of the project')
    parser.add_argument('-z', metavar='number', type=int, 
            help='number of concurrent processes to use in parallel mode')

    args = parser.parse_args()
    
    # return the values of arguments
    return {'group':args.g, 'host':args.H, 'project':args.p, 'task':args.t, 'number':args.z}

def fab_execute(**kwargs):
    """Execute the task from service/{taskname}.py with class FabricSupport."""

    # get values from the given tuple
    project = kwargs['project']
    host = kwargs['host']
    task = kwargs['task']

    # give the concurrent number a default value
    number = kwargs.get('number', "1")
    
    # change the multiple hosts into a list
    hosts = host.split(',')

    # get the username and keyfile path from conf/auth.ini
    useropts = userconf()

    # import class FabricSupport from the given task
    get_import = "from service.{0} import FabricSupport".format(project)
    exec get_import

    # execute the given task
    myfab = FabricSupport()
    return myfab.execute(task,hosts,number,useropts["user"],useropts["keyfile"])

def run_task_from_db(opts):
    """Get the hosts from database, and run fab_execute."""

    # get the database from conf/db.ini
    dbopts = dbconf()

    # connect the database
    db = Connection(dbopts["host"], dbopts["database"], dbopts["user"], dbopts["password"])

    # get the hosts from database
    sql = """SELECT * FROM host WHERE hostgroup_name = '{0}'""".format(opts["group"])
    result = []
    for item in db.query(sql):
        result.append(item.ec2_local_hostname)
    host = ','.join(result)

    # run fab_execute
    if not host:
        print "No host(s) found in group \"{0}\"".format(opts["group"])
        return
    if not opts["number"]:
        return fab_execute(project=opts["project"],host=host,task=opts["task"])
    return fab_execute(project=opts["project"],host=host,number=opts["number"],task=opts["task"])

def run_task_from_value(opts):
    """Get the hosts from given arguments, and run fab_execute. """

    # run fab_execute
    if not opts["host"]:
        print "A group or host(s) is required."
        return
    if not opts["number"]:
        return fab_execute(project=opts["project"],host=opts["host"],task=opts["task"])
    return fab_execute(project=opts["project"],host=opts["host"],number=opts["number"],task=opts["task"])

def run_task(opts):
    """Determine which run_task_from should be triggered."""

    if not opts["group"]:
        return run_task_from_value(opts)
    return run_task_from_db(opts)

def main():
    # check if user executes the script without any arguments
    argv_len = len(sys.argv)
    if argv_len < 2:
        os.system("./ddep.py -h")
        return None 

    # get the arguments and trigger the run_task
    opts = parse_opts()
    run_task(opts)

if __name__=='__main__':
    main()
