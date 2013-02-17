from reference_parser import *

__author__ = 'jason'


class Annotation(object):
    """A text annotation to a scriptural reference"""

    def __init__(self, reference, text):
        self.reference = reference
        self.text = text

    def __repr__(self):
        return "Annotation: %s: %s" % (self.reference, self.text)


class AnnotationManager(dict):
    """A specialized dictionary to hold Annotation objects in string
    categories"""

    def __init__(self):
        dict.__init__(self)

    def annotations(self, rng, category=None):
        """Return all the annotations associated with the specified
        range of scripture text, optionally limited to a single category"""
        if category:
            return [note for note in self[category]
                    if rng.contains(note.reference)]
        else:
            notes = []
            for category in self.keys():
                notes.extend(self.annotations(rng, category))
            return notes

if __name__ == "__main__":
    man = AnnotationManager()
    note = Annotation(ReferenceParser().parse("John 2"), "This is a test annotation.")
    man["annotations"] = []
    man["annotations"].append(note)
    print man.annotations(ReferenceParser().parse("John 1-3"))
