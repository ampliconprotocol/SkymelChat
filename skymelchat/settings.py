#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

#######################################################################
#
# Load and save user settings
#
#######################################################################


import os
import json

from skymelchat  import paths


def load_settings(settings_file=paths.PATH_SKYMELCHAT_USER_CONFIG_FILE):
    settings_json = json.loads('{}')
    if os.path.isfile(settings_file):
        with open(settings_file) as json_file:
            settings_json = json.load(json_file)
        paths.SETTINGS = settings_json


def save_settings(settings_dict=paths.SETTINGS, settings_file=paths.PATH_SKYMELCHAT_USER_CONFIG_FILE):
    with open(settings_file, 'w') as json_file:
        json_file.write(json.dumps(settings_dict, indent=4, ensure_ascii=False))
