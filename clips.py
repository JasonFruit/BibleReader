import cPickle

__author__ = 'jason'

class ClipManager(object):
    def __init__(self):
        self.categories = {"unclassified": []}

    def add(self, clip, category="unclassified"):
        try:
            self.categories[category].append(clip)
        except KeyError:
            self.categories[category] = [clip]

    def add_category(self, category):
        self.categories[category] = []

    def remove_category(self, category):
        self.categories.remove(category)

    def delete(self, clip, category="unclassified"):
        self.categories[category].remove(clip)


class Clip(object):
    def __init__(self, title, html):
        self.title = title
        self.html = html


def save_to_file(filename, manager):
    cPickle.dump(manager, open(filename, "wb"))


def load_from_file(filename):
    return cPickle.load(open(filename, "rb"))

if __name__ == "__main__":
    clip_manager = ClipManager()
    clip_manager.add(Clip("Test 1", ""))
    clip_manager.add(Clip("Test 2", ""))
    clip_manager.add(Clip("Test 3", ""))
    save_to_file("clips.brc", clip_manager)