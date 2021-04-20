#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  18 00:29:35 2021

@author: arslan
"""

import numpy as np
import numpy.ctypeslib as npct
from ctypes import c_int, c_double
import pathlib

# input type for the cos_doubles function
# must be a double array, with single dimension that is contiguous
array_2d_double = npct.ndpointer(dtype=np.double, ndim=2, flags='CONTIGUOUS')
array_1d_double = npct.ndpointer(dtype=np.double, ndim=1, flags='CONTIGUOUS')

# load the library, using numpy mechanisms
path = pathlib.Path(__file__).parent.parent.absolute()
libcd = npct.load_library("typereduction", str(path))

# setup the return types and argument types
libcd.EIASC_algorithm.restype = c_double
libcd.EIASC_algorithm.argtypes = [array_2d_double, array_1d_double, c_int, array_1d_double]


def EIASC_algorithm(intervals, params=np.array([])):
    o = np.zeros(shape=(4, ))
    libcd.EIASC_algorithm(intervals, params, len(intervals), o)
    return o



