#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

#######################################################################
#
# Python Factory UI paths.py
# All paths needed for the application, according to the system
#
#######################################################################

import os
import sys
import tempfile
import subprocess
from inspect import getsourcefile
from collections import OrderedDict

PATH_SKYMELCHAT = os.path.dirname(getsourcefile(lambda: 0))

PATH_HOME = os.path.expanduser("~")
PATH_REAL_HOME = PATH_HOME

ACTUAL_OS = 'linux'

tempdir = tempfile.TemporaryDirectory()
PATH_SKYMELCHAT_TMP = tempdir.name
PATH_SKYMELCHAT_USER_CONFIG_FOLDER = os.path.join(PATH_HOME, '.config', 'skymelchat')

if sys.platform == 'darwin':
    PATH_SKYMELCHAT_USER_CONFIG_FOLDER = os.path.join(PATH_HOME, 'Library', 'Application Support', 'skymelchat')
    ACTUAL_OS = 'macos'
elif sys.platform == 'win32' or os.name == 'nt':
    PATH_SKYMELCHAT = os.path.abspath(os.path.dirname(sys.argv[0]))
    PATH_SKYMELCHAT_USER_CONFIG_FOLDER = os.path.join(os.getenv('LOCALAPPDATA'), 'skymelchat')
    ACTUAL_OS = 'windows'
else:
    try:
        with subprocess.Popen(['getent', 'passwd', str(os.getuid())], stdout=subprocess.PIPE) as proc:
            PATH_REAL_HOME = proc.stdout.read().decode().split(':')[5]
    except FileNotFoundError:
        pass
    if not os.path.isdir(os.path.join(PATH_HOME, '.config')):
        os.mkdir(os.path.join(PATH_HOME, '.config'))

if not os.path.isdir(PATH_SKYMELCHAT_USER_CONFIG_FOLDER):
    os.mkdir(PATH_SKYMELCHAT_USER_CONFIG_FOLDER)

PATH_SKYMELCHAT_GRAPHICS = os.path.join(PATH_SKYMELCHAT, 'graphics')

PATH_SKYMELCHAT_LOCALE = os.path.join(PATH_SKYMELCHAT, 'locale')

PATH_SKYMELCHAT_USER_CONFIG_FILE = os.path.join(PATH_SKYMELCHAT_USER_CONFIG_FOLDER, 'config.json')

def get_graphics_path(filename):
    final_filepath = os.path.join(PATH_SKYMELCHAT_GRAPHICS, filename)
    if sys.platform == 'win32' or os.name == 'nt':
        final_filepath = final_filepath.replace('\\', '/')
    return final_filepath

SETTINGS = {
    'available_wallets': []
}

SESSION = {
    'selected_wallet': False,
    'selected_conversation': False,
    'conversations': OrderedDict()
}