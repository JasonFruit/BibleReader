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

    def move(self, clip, from_category, to_category):
        # remove the clip from the old category
        self.categories[from_category].remove(clip)

        # if the new category exists, add the clip to it;
        # otherwise, create the new category with the clip in it
        try:
            self.categories[to_category].append(clip)
        except KeyError:
            self.categories[to_category] = [clip]


class Clip(object):
    def __init__(self, title, html):
        self.title = title
        self.html = html


def save_to_file(filename, manager):
    cPickle.dump(manager, open(filename, "wb"))


def load_from_file(filename):
    return cPickle.load(open(filename, "rb"))
