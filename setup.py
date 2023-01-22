#!/usr/bin/env python3

#######################################################################
#
# SkymelChat setup.py
# Install as a python package using `python3 setup.py install`
#
#######################################################################

import os
import sys
import pydoc

from setuptools import setup, find_namespace_packages

import skymelchat


def get_description(filename='README.md'):
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename), encoding='utf-8') as f:
        file = list(f)
    desc = ''
    for item in file[11: len(file)]:
        desc += item
    return desc


def get_data_files():
    files = []
    if sys.platform.startswith('linux') and 'QT_APPIMAGE' not in os.environ.keys():
        appid = skymelchat.__desktopid__
        print(os.getcwd())
        files = [
            ('share/icons/hicolor/16x16/apps', ['skymelchat/graphics/icons/16x16/{}.png'.format(appid)]),
            ('share/icons/hicolor/22x22/apps', ['skymelchat/graphics/icons/22x22/{}.png'.format(appid)]),
            ('share/icons/hicolor/24x24/apps', ['skymelchat/graphics/icons/24x24/{}.png'.format(appid)]),
            ('share/icons/hicolor/32x32/apps', ['skymelchat/graphics/icons/32x32/{}.png'.format(appid)]),
            ('share/icons/hicolor/48x48/apps', ['skymelchat/graphics/icons/48x48/{}.png'.format(appid)]),
            ('share/icons/hicolor/64x64/apps', ['skymelchat/graphics/icons/64x64/{}.png'.format(appid)]),
            ('share/icons/hicolor/128x128/apps', ['skymelchat/graphics/icons/128x128/{}.png'.format(appid)]),
            ('share/icons/hicolor/256x256/apps', ['skymelchat/graphics/icons/256x256/{}.png'.format(appid)]),
            ('share/icons/hicolor/512x512/apps', ['skymelchat/graphics/icons/512x512/{}.png'.format(appid)]),
            ('share/icons/hicolor/scalable/apps', ['skymelchat/graphics/icons/scalable/{}.svg'.format(appid)]),
            # ('share/applications', ['data/{}.desktop'.format(appid)]),
            # ('share/metainfo', ['data/appdata/{}.appdata.xml'.format(appid)]),
            # ('share/mime/packages', ['data/mime/{}.xml'.format(appid)]),
            # ('share/doc/skymelchat', ['CHANGELOG', 'LICENSE', 'README.md'])
        ]

    return files


def get_package_files():
    files = {}

    files['skymelchat'] = [
        'locale/*',
        'graphics/*',
        # 'app/data/*',
    ]

    return files


def pip_notes():
    os.system('cls' if sys.platform == 'win32' else 'clear')
    pydoc.pager('''
    https://skymel.com
''')


# --------------------------------------------------------------------------- #

setup_requires = [
    'setuptools',
    # 'py2app',
    'install_freedesktop'
]
install_requires = [
    'PyQt6',
    'python-i18n',
    'lorem'
]

# --------------------------------------------------------------------------- #

try:
    # begin setuptools installer
    result = setup(
        app=['skymelchat/__main__.py'],
        name=skymelchat.__appname__.lower(),
        version=skymelchat.__version__,
        author=skymelchat.__author__,
        author_email=skymelchat.__email__,
        description='SkymelChat',
        long_description=get_description(),
        url=skymelchat.__website__,
        license='Proprietary',
        packages=find_namespace_packages(include=['skymelchat', 'skymelchat.*']),
        setup_requires=setup_requires,
        install_requires=install_requires,
        data_files=get_data_files(),
        package_data=get_package_files(),
        include_package_data=True,
        entry_points={'gui_scripts': ['skymelchat=skymelchat.__main__:main']},
        keywords='skymelchat',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: X11 Applications :: Qt',
            'Intended Audience :: End Users/Desktop',
            'License :: Proprietary',
            'Natural Language :: English',
            'Operating System :: POSIX',
            'Topic :: Tools',
            'Programming Language :: Python :: 3 :: Only'
        ],
        options={
            'py2app': {
                'argv_emulation': True,
                # 'iconfile': 'src/Icon.icns',  # optional
                # 'plist': 'src/Info.plist',    # optional
            }
        },
        desktop_entries={
            'skymelchat': {
                'Name': 'SkymelChat',
                'Categories': 'Utility;ArtificialIntelligence;',
            },
        },
    )
except BaseException:
    if skymelchat.__ispypi__:
        pip_notes()
    raise
