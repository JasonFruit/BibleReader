__author__ = 'jason'

import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

from .bible_reader import BibleReaderModel
from .books import books_order
from .rc import *
from .first_run import *
from annotations import *
from annotations_ui import *

app = QApplication(sys.argv)

app_name = "Bible Reader"


class PassageSelector(QDialog):
    """Convenient interface for choosing a passage of scripture"""

    def __init__(self):
        QDialog.__init__(self)
        self.setModal(True)
        self.setWindowTitle("Passage Lookup")

        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # a combo-box of books, in order of appearance
        self.book = QComboBox(self)
        self.book.addItems(books_order)

        self.layout.addRow("&Book:", self.book)

        # the rest of the reference is plain text; maybe eventually
        # write a validator function
        self.section = QLineEdit(self)
        self.layout.addRow("&Section", self.section)

        # space before the buttons
        self.layout.addRow(QLabel(""))
        self.layout.addRow(QLabel(""))

        # A button to look up the passage
        self.lookup = QPushButton("&Look up", self)
        self.lookup.setMaximumWidth(120)
        self.layout.addRow("", self.lookup)

    def ref(self):
        """return a string representation of the passage reference"""
        return "%s %s" % (books_order[self.book.currentIndex()],
                          self.section.text())

    def run(self, success_callback):
        """show the form and call success_callback when finished"""
        self.lookup.clicked.connect(success_callback)
        self.show()


class OverlayButton(QPushButton):
    def __init__(self, text, parent=None):
        QPushButton.__init__(self, text, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Button, Qt.transparent)
        palette.setColor(palette.Shadow, Qt.transparent)
        palette.setColor(palette.Dark, Qt.transparent)
        self.setPalette(palette)


class BibleReader(QMainWindow, BibleReaderModel):
    """The main UI for the bible reader app"""

    def __init__(self):
        QMainWindow.__init__(self)
        BibleReaderModel.__init__(self)

        self.parser = ReferenceParser()
        self.annotations = AnnotationManager()

        map(self.annotations.add_category,
            ["Cat 1", "Cat 2", "Cat 3"])

        self.setWindowTitle(app_name)

        # add the main scripture display widget
        self.display = QWebView(self)
        self.display.setMinimumSize(600, 400)

        # it's all that's contained in this main window
        self.setCentralWidget(self.display)

        # the passage selection menu
        self.passage_menu = self.menuBar().addMenu("&Passage")

        self.set_up_passage_menu()

        self.view_menu = self.menuBar().addMenu("Vie&w")
        self.set_up_view_menu()

        self.annotation_menu = self.menuBar().addMenu("&Annotations")
        self.set_up_annotation_menu()

        self.add_shortcuts()
        self.lookup(self.last_passage)

        app.lastWindowClosed.connect(self.save_rc)

    def toggle_fullscreen(self):

        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

        self.resizeEvent()

    def add_shortcuts(self):
        fullscreen_shortcut = QShortcut(QKeySequence(self.tr("Alt+F")), self)
        fullscreen_shortcut.activated.connect(self.toggle_fullscreen)

        lookup_shortcut = QShortcut(QKeySequence(self.tr("Ctrl+L")), self)
        lookup_shortcut.activated.connect(self.interactive_lookup)

        browse_shortcut = QShortcut(QKeySequence(self.tr("Ctrl+B")), self)
        browse_shortcut.activated.connect(self.browse)

        print_shortcut = QShortcut(QKeySequence(self.tr("Ctrl+P")), self)
        print_shortcut.activated.connect(self.print_)

        # on Windows or Unix window managers that don't map F11 to
        # fullscreen, do it for them
        fullscreen_shortcut = QShortcut(QKeySequence(self.tr("F11")), self)
        fullscreen_shortcut.activated.connect(self.toggle_fullscreen)

    def set_up_passage_menu(self):
        # menu option to look up a passage
        lookup_action = QAction("&Look up", self)
        lookup_action.triggered.connect(self.interactive_lookup)

        # add it to the passage menu
        self.passage_menu.addAction(lookup_action)

        # menu option to browse for a passage
        browse_action = QAction("&Browse", self)
        browse_action.triggered.connect(self.browse)

        # add it to the passage menu
        self.passage_menu.addAction(browse_action)

        print_action = QAction("&Print", self)
        print_action.triggered.connect(self.print_)
        self.passage_menu.addAction(print_action)

    def print_(self):
        printDialog = QPrintDialog()
        if printDialog.exec_() == QDialog.Accepted:
            self.display.print_(printDialog.printer())

    def set_up_view_menu(self):
        font_menu = self.view_menu.addMenu("&Font")
        font_db = QFontDatabase()
        families = font_db.families()
        for family in families:
            action = QAction(family, self)

            def font_cb(family):
                def callback():
                    self.font = family
                    try:
                        self.lookup(self.last_passage)
                    except:
                        pass

                return callback

            action.triggered.connect(font_cb(family))
            font_menu.addAction(action)

    def resizeEvent(self, event=None):
        if self.isFullScreen():
            self.menuBar().hide()
        else:
            self.menuBar().show()

    def browse(self):
        pl = PassageSelector()

        def doit():
            self.lookup(pl.ref())
            pl.hide()

        pl.run(doit)

    def interactive_lookup(self):
        passage_ref, ok = QInputDialog.getText(self,
                                               'Passage Lookup',
                                               'Passage reference:')

        if ok:
            self.lookup(passage_ref)

    def set_up_annotation_menu(self):
        add_action = QAction("&Add", self)
        add_action.triggered.connect(self.add_annotation)
        self.annotation_menu.addAction(add_action)

    def add_annotation(self):
        passage_ref = self.last_passage

        if len(self.annotations.keys()) > 0:
            category, ok = QInputDialog.getItem(self, "Annotation Category",
                                                "Category:",
                                                self.annotations.keys())
        else:
            category, ok = "uncategorized", True

        if ok:
            note = Annotation(self.parser.parse(passage_ref),
                              "")
            dlg = AnnotationDialog(note, self)

            def add_note():
                self.annotations[category].append(note)

            dlg.accepted.connect(add_note)
            dlg.exec_()

    def lookup(self, passage_ref):
        self.display.setHtml(self.get_html(passage_ref))


def main():
    if not rc_exists():
        first_run()

    reader = BibleReader()
    reader.showMaximized()
    app.exec_()
