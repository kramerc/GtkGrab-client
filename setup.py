#!/usr/bin/env python2
from distutils.core import setup

setup(name='GtkGrab-client',
      version='0.3.0',
      description='Automatic screenshot upload utility',
      license='GNU GPLv3',
      maintainer='Pieter Kokx',
      maintainer_email='pieter@kokx.nl',
      py_modules=['pyperclip'],
      scripts=['GtkGrab','record-gif.sh'],
      data_files=[('share/GtkGrab-client', ['config.cfg-sample-linux','config.cfg-sample-mac']),
                  ('share/licenses/GtkGrab-client', ['COPYING'])],
      url='https://github.com/kokx/GtkGrab-client')
