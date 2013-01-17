__author__ = 'jason'

import os
from PySide.QtCore import QDir

default_rc = {"font": "sans",
              "version": "esv",
              "init_passage": "John 3"}

def rc_dir():
    return os.path.join(QDir.home().absolutePath(), ".biblereader")

def rc():
    return os.path.join(rc_dir(), "rc")

def clip_rc():
    return os.path.join(rc_dir(), "clips")

def rc_exists():
    return (os.path.isdir(rc_dir()) and
            os.path.exists(rc()) and
            os.path.exists(clip_rc()))