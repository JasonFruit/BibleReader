__author__ = 'jason'

import os
from .rc import *
from .clips import *
import pickle

def first_run():
    os.mkdir(rc_dir())
    pickle.dump(default_rc, open(rc(), "wb"))
    pickle.dump(ClipManager(), open(clip_rc(), "wb"))
