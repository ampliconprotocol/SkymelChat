#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

#######################################################################
#
#
# Load and set locale settings
#
#######################################################################


import os
import i18n

from skymelchat import paths

i18n.set('file_format', 'json')
i18n.load_path.append(paths.PATH_SKYMELCHAT_LOCALE)
i18n.set('filename_format', '{locale}.{format}')
i18n.set('skip_locale_root_data', True)
i18n.set('fallback', 'en')


def _(text):
    return i18n.t(text)


def load_translation_files():
    for lp in i18n.load_path:
        for f in os.listdir(lp):
            path = os.path.join(lp, f)
            if os.path.isfile(path) and path.endswith(i18n.config.get('file_format')):
                locale = f.split(i18n.config.get('namespace_delimiter'))[0]
                if '{locale}' in i18n.config.get('filename_format'):
                    i18n.resource_loader.load_translation_file(f, lp, locale)


def set_language(language):
    i18n.set('locale', language)


def get_language_pairs(language):
    result = i18n.translations.container.get(language, {})
    return result


def get_available_language_names(inverted=False):
    final_dict = {}
    for language in i18n.translations.container:
        final_dict[language] = i18n.translations.container[language].get('language_name', '')
    if inverted:
        final_dict = {v: k for k, v in final_dict.items()}
    return final_dict
