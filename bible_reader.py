from clips import *
from bibles import Bible
import rc
import pickle

def read_rc():

    try:
        tmp_rc = pickle.load(open(rc.rc(), "rb"))
    except:
        return rc.default_rc
    
    for key in rc.default_rc.keys():
        try:
            tmp_rc[key]
        except KeyError:
            tmp_rc[key] = rc.default_rc[key]
            
    return tmp_rc

def write_rc(the_rc):
    pickle.dump(the_rc, open(rc.rc(), "wb"))

class BibleReaderModel(object):
    def __init__(self):
        self.rc = read_rc()
        self.versions = ["akjv", "asv", "douayrheims", "esv",
                         "kjv", "net", "web", "ylt"]

        self.version = self.rc["version"]
        self.clip_manager = load_from_file(rc.clip_rc())
        self.font = self.rc["font"]
        self.last_passage = self.rc["init_passage"]

    def get_html(self, passage_ref):
        self.last_passage = passage_ref
        bible = Bible(self.version, font=self.font)
        return bible.query(passage_ref)

    def add_clip(self, title, html, category="unclassified"):
        clip = Clip(title, html)
        self.clip_manager.add(clip, category)
        save_to_file(rc.clip_rc(), self.clip_manager)

    def save_rc(self):
        self.rc["version"] = self.version
        self.rc["font"] = self.font
        self.rc["init_passage"] = self.last_passage
        write_rc(self.rc)
