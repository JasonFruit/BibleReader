from clips import *
from bibles import Bible

class BibleReaderModel(object):
    def __init__(self):
        self.versions = ["akjv", "asv", "douayrheims", "esv",
                         "kjv", "net", "web", "ylt"]
        self.version = self.versions[0]
        self.clip_manager = load_from_file("clips.brc")
        self.font = "Helvetica"
        self.last_passage = "John 3"

    def get_html(self, passage_ref):
        self.last_passage = passage_ref
        bible = Bible(self.version, font=self.font)
        return bible.query(passage_ref)

    def add_clip(self, title, html):
        clip = Clip(title, html)
        self.clip_manager.add(clip)
        save_to_file("clips.brc", self.clip_manager)

