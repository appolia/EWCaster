#! /usr/bin/env python

from distutils.core import setup, Extension

import sys

# from an original source code by Joachim Kaeber (kaeber@gmd.de)

_ext_modules = None

if sys.platform in ['linux2', 'solaris2', 'win32']:
    _ext_modules = [ Extension('dvbobjects.utils._crc32', [ 'sectioncrc.py.c'] ), ]

setup(
    name = "dvbobjects",
    version = "0.2",
    description = "Python Package for dvb-ews Indonesia transport stream data generation",
    author = "Lorenzo Pallara, Riza Azmi",
    author_email = "l.pallara@avalpa.com, riza.azmi@kominfo.go.id",
    url = "",
    
    packages = [
        'dvbobjects',
        'dvbobjects.DSMCC',
        'dvbobjects.DSMCC.BIOP',
        'dvbobjects.DVB',
        'dvbobjects.MHP',
        'dvbobjects.HBBTV',
	'dvbobjects.PSI',
        'dvbobjects.MPEG',
        'dvbobjects.SBTVD',
        'dvbobjects.utils',
        'dvbobjects.EWS',
        ],

    ext_modules = _ext_modules
)
