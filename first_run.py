__author__ = 'jason'

import os
import rc
import clips
import pickle

def first_run():
    os.mkdir(rc.rc_dir())
    pickle.dump(rc.default_rc, open(rc.rc(), "wb"))
    pickle.dump(clips.ClipManager(), open(rc.clip_rc(), "wb"))
