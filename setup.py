#!/usr/bin/python

#Audio Tools, a module and set of tools for manipulating audio data
#Copyright (C) 2007-2012  Brian Langenberger

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

VERSION = '2.18alpha4'

import sys

if (sys.version_info < (2, 5, 0, 'final', 0)):
    print >> sys.stderr, "*** Python 2.5.0 or better required"
    sys.exit(1)

from distutils.core import setup, Extension
import subprocess
import re


def pkg_config(package, option):
    sub = subprocess.Popen(["pkg-config", option, package],
                           stdout=subprocess.PIPE)
    spaces = re.compile('\s+', re.DOTALL)
    args = spaces.split(sub.stdout.read().strip())
    sub.stdout.close()
    sub.wait()
    return args


cdiomodule = Extension('audiotools.cdio',
                       sources=['src/cdiomodule.c'],
                       libraries=['cdio', 'cdio_paranoia',
                                  'cdio_cdda', 'm'])

resamplemodule = Extension('audiotools.resample',
                           sources=['src/resample.c'])

pcmmodule = Extension('audiotools.pcm',
                      sources=['src/pcm.c'])

replaygainmodule = Extension('audiotools.replaygain',
                             sources=['src/replaygain.c'])

decodersmodule = Extension('audiotools.decoders',
                           sources=['src/array.c',
                                    'src/array2.c',
                                    'src/pcmconv.c',
                                    'src/common/md5.c',
                                    'src/bitstream.c',
                                    'src/huffman.c',
                                    'src/decoders/flac.c',
                                    'src/decoders/oggflac.c',
                                    'src/common/flac_crc.c',
                                    'src/common/ogg_crc.c',
                                    'src/decoders/shn.c',
                                    'src/decoders/alac.c',
                                    'src/decoders/wavpack.c',
                                    'src/decoders/vorbis.c',
                                    'src/decoders/mlp.c',
                                    'src/decoders/aobpcm.c',
                                    'src/decoders/sine.c',
                                    'src/decoders/ogg.c',
                                    'src/decoders.c'],
                           define_macros=[("VERSION", VERSION)])

encodersmodule = Extension('audiotools.encoders',
                           sources=['src/array.c',
                                    'src/array2.c',
                                    'src/pcmconv.c',
                                    'src/bitstream.c',
                                    'src/pcmreader.c',
                                    'src/common/md5.c',
                                    'src/encoders/flac.c',
                                    'src/common/flac_crc.c',
                                    'src/common/misc.c',
                                    'src/encoders/shn.c',
                                    'src/encoders/alac.c',
                                    'src/encoders/wavpack.c',
                                    'src/encoders.c'],
                           define_macros=[("VERSION", VERSION)])

bitstreammodule = Extension('audiotools.bitstream',
                            sources=['src/mod_bitstream.c',
                                     'src/bitstream.c',
                                     'src/huffman.c'])

verifymodule = Extension('audiotools.verify',
                         sources=['src/verify.c',
                                  'src/common/ogg_crc.c',
                                  'src/bitstream.c'])

extensions = [resamplemodule,
              pcmmodule,
              replaygainmodule,
              decodersmodule,
              encodersmodule,
              bitstreammodule,
              verifymodule]

if (sys.platform == 'linux2'):
    extensions.append(Extension(
            'audiotools.prot',
            sources=['src/prot.c',
                     'src/prot/cppm.c',
                     'src/prot/ioctl.c',
                     'src/prot/dvd_css.c'],
            define_macros=[('DVD_STRUCT_IN_LINUX_CDROM_H', None),
                           ('HAVE_LINUX_DVD_STRUCT', None)]))
elif (sys.platform == 'darwin'):
    extensions.append(Extension(
            'audiotools.prot',
            sources=['src/prot.c',
                     'src/prot/cppm.c',
                     'src/prot/ioctl.c',
                     'src/prot/dvd_css.c'],
            define_macros=[('DARWIN_DVD_IOCTL', None)]))
else:
    #don't install the protection module on
    #unsupported platformats
    pass


setup(name='Python Audio Tools',
      version=VERSION,
      description='A collection of audio handling utilities',
      author='Brian Langenberger',
      author_email='tuffy@users.sourceforge.net',
      url='http://audiotools.sourceforge.net',
      packages=["audiotools",
                "audiotools.py_decoders", "audiotools.py_encoders"],
      ext_modules=extensions,
      data_files=[("/etc", ["audiotools.cfg"])],
      scripts=["cd2track", "cdinfo", "cdplay",
               "track2track", "trackrename", "trackinfo",
               "tracklength", "track2cd", "trackcmp", "trackplay",
               "tracktag", "audiotools-config",
               "trackcat", "tracksplit",
               "tracklint", "trackverify",
               "coverdump", "coverview", "record2track",
               "dvdainfo", "dvda2track"])
