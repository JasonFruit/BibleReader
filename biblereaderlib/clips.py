import cPickle

__author__ = 'jason'

class ClipManager(object):
    """Represents a categorized collection of clips"""
    def __init__(self):
        self.categories = {"unclassified": []}

    def add(self, clip, category="unclassified"):
        """Add a clip in the specified category, or 'unclassified' if
        none is specified"""
        try:
            self.categories[category].append(clip)
        except KeyError:
            self.categories[category] = [clip]

    def add_category(self, category):
        """Add a new empty category, if it doesn't already exist"""
        if not category in self.categories.keys():
            self.categories[category] = []

    def remove_category(self, category):
        """Remove the specified category"""
        self.categories.remove(category)

    def delete(self, clip, category="unclassified"):
        """Remove the specified clip from the specified category (the
        same clip can exist in multiple categories)"""
        self.categories[category].remove(clip)

    def move(self, clip, from_category, to_category):
        """Move a clip from one category to another"""
        
        # remove the clip from the old category
        self.categories[from_category].remove(clip)

        # if the new category exists, add the clip to it;
        # otherwise, create the new category with the clip in it
        try:
            self.categories[to_category].append(clip)
        except KeyError:
            self.categories[to_category] = [clip]


class Clip(object):
    """Represents a titled clip of HTML scripture"""
    def __init__(self, title, html):
        self.title = title
        self.html = html


def save_to_file(filename, manager):
    """Save the specified ClipManager to the specified filename"""
    cPickle.dump(manager, open(filename, "wb"))


def load_from_file(filename):
    """Load a clip manager from the specified filename"""
    return cPickle.load(open(filename, "rb"))
