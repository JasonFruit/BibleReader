__author__ = 'jason'

import os
from PySide.QtCore import QDir

# the rc that is used if none exists or the current one is otherwise
# unrecoverable
default_rc = {"font": "sans",
              "version": "esv",
              "init_passage": "John 3"}

def rc_dir():
    """Return the directory that contains the rc files"""
    return os.path.join(QDir.home().absolutePath(), ".biblereader")

def rc():
    """Return the path to the main rc file"""
    return os.path.join(rc_dir(), "rc")

def clip_rc():
    """Return the path to the clip rc file"""
    return os.path.join(rc_dir(), "clips")

def rc_exists():
    """Check if all the elements of the rc directory exist"""
    return (os.path.isdir(rc_dir()) and
            os.path.exists(rc()))
