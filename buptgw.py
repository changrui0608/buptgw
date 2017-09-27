#!/usr/bin/env python

usage = \
"""
BUPT Gateway Untility
Login, logout, and check statistics.

Usage: buptgw.py < login | logout | stats >  [options]

Options:
    -u  --user          <username>  Specify the gateway account username.
    -p  --password      <password>  Specify the gateway account password.

"""

import urllib
import urllib2
import getpass
import re
import sys


gateway_url = "http://gw.bupt.edu.cn/"
logout_url  = "http://gw.bupt.edu.cn/F.htm"


def login(username=None, password=None):
    if username is None:
        username = raw_input("Username: ")
    if password is None:
        password = getpass.getpass("Password: ")
    username, password = str(username), str(password)
    data = urllib.urlencode({
        'DDDDD': username,
        'upass': password,
        'savePWD': '0',
        '0MKKey': ''
        })
    res = urllib2.urlopen(gateway_url, data)
    res_content = unicode(res.read(), 'gb2312')
    if 'successfully' in res_content:
        print "You have successfully logged into our system."
        print "Please don't forget to log out after you have finished."
        print ""
        sys.exit()
    else:
        print "Login ERROR!"
        print ""
        sys.exit()


def logout():
    res = urllib2.urlopen(logout_url)
    res_content = unicode(res.read(), 'gb2312')
    if 'Msg=14' in res_content:
        print "Logout successfully."
        print ""
        sys.exit()
    else:
        print "Logout ERROR!"
        print ""
        sys.exit()


def stats():
    res = urllib2.urlopen(gateway_url)
    res_content = unicode(res.read(), 'gb2312')


def dis_help_and_exit():
    print usage
    sys.exit()


if __name__ == '__main__':

    action = None
    username, password = None, None
    skip_flag = False

    for index, arg in enumerate(sys.argv):

        if skip_flag:
            skip_flag = False
            continue

        if arg in ['login', 'logout', 'stats']:
            if action is not None:    # if multiple actions in exec parameter
                dis_help_and_exit()
            # action = locals()[arg.lower()]    # set action, will be executed later
            action = arg

        if arg in ['-u', '--user']:
            skip_flag = True
            try:
                username = sys.argv[index + 1]
            except IndexError:
                dis_help_and_exit()

        if arg in ['-p', '--password']:
            skip_flag = True
            try:
                password = sys.argv[index + 1]
            except IndexError:
                dis_help_and_exit()
    

    if action:
        if action == 'login':
            login(username, password)
        elif action == 'logout':
            logout()
        elif action == 'stats':
            stats()
        else:
            dis_help_and_exit()
    else:
        dis_help_and_exit()


