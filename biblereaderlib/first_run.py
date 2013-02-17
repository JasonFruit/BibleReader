__author__ = 'jason'

import os
from .rc import *
import pickle

def first_run():
    os.mkdir(rc_dir())
    pickle.dump(default_rc, open(rc(), "wb"))
