from clips import *
from bibles import Bible
import rc
import pickle

class BibleReaderModel(object):
    def __init__(self):
        my_rc = pickle.load(open(rc.rc(), "rb"))
        self.versions = ["akjv", "asv", "douayrheims", "esv",
                         "kjv", "net", "web", "ylt"]

        self.version = my_rc["version"]
        self.clip_manager = load_from_file(rc.clip_rc())
        self.font = my_rc["font"]
        self.last_passage = my_rc["init_passage"]

    def get_html(self, passage_ref):
        self.last_passage = passage_ref
        bible = Bible(self.version, font=self.font)
        return bible.query(passage_ref)

    def add_clip(self, title, html, category="unclassified"):
        clip = Clip(title, html)
        self.clip_manager.add(clip, category)
        save_to_file(rc.clip_rc(), self.clip_manager)