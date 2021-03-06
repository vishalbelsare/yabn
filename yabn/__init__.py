# __init__.py: Yet Another Bayes Net library
# Contact: Jacob Schreiber ( jmschreiber91@gmail.com )

"""
For detailed documentation and examples, see the README.
"""

# Make our dependencies explicit so compiled Cython code won't segfault trying
# to load them.
import networkx, matplotlib.pyplot, scipy

import numpy as np
import os
import pyximport




# Adapted from Cython docs https://github.com/cython/cython/wiki/
# InstallingOnWindows#mingw--numpy--pyximport-at-runtime
if os.name == 'nt':
    if 'CPATH' in os.environ:
        os.environ['CPATH'] = os.environ['CPATH'] + np.get_include()
    else:
        os.environ['CPATH'] = np.get_include()

    # XXX: we're assuming that MinGW is installed in C:\MinGW (default)
    if 'PATH' in os.environ:
        os.environ['PATH'] = os.environ['PATH'] + ';C:\MinGW\bin'
    else:
        os.environ['PATH'] = 'C:\MinGW\bin'

    mingw_setup_args = { 'options': { 'build_ext': { 'compiler': 'mingw32' } } }
    pyximport.install(setup_args=mingw_setup_args)

elif os.name == 'posix':
    if 'CFLAGS' in os.environ:
        os.environ['CFLAGS'] = os.environ['CFLAGS'] + ' -I' + np.get_include()
    else:
        os.environ['CFLAGS'] = ' -I' + np.get_include()

    pyximport.install()


from yabn import *

__version__ = '0.1.0'