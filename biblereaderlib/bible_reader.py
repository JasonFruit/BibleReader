from .bibles import Bible
from .rc import *
import pickle

def read_rc():

    try:
        tmp_rc = pickle.load(open(rc(), "rb"))
    except:
        return default_rc
    
    for key in default_rc.keys():
        try:
            tmp_rc[key]
        except KeyError:
            tmp_rc[key] = default_rc[key]
            
    return tmp_rc

def write_rc(the_rc):
    pickle.dump(the_rc, open(rc(), "wb"))

class BibleReaderModel(object):
    def __init__(self):
        self.rc = read_rc()
        self.versions = ["akjv", "asv", "douayrheims", "esv",
                         "kjv", "net", "web", "ylt"]

        self.version = self.rc["version"]
        self.font = self.rc["font"]
        self.last_passage = self.rc["init_passage"]

    def get_html(self, passage_ref):
        self.last_passage = passage_ref
        bible = Bible(self.version, font=self.font)
        return bible.query(passage_ref)

    def save_rc(self):
        self.rc["version"] = self.version
        self.rc["font"] = self.font
        self.rc["init_passage"] = self.last_passage
        write_rc(self.rc)
