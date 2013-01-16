__author__ = 'jason'

import sys

from bible_reader import BibleReaderModel
from books import books_order
from clips import *

from PySide.QtGui import *
from PySide.QtWebKit import *

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

class ClipListViewer(QWidget):
    def __init__(self, category, clips, manager, manager_ui, parent=None):
        QWidget.__init__(self, parent)
        self.category = category
        self.clips = clips
        self.manager = manager
        self.manager_ui = manager_ui
        self.set_up_ui()

    def set_up_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.keys = [clip.title for clip in self.clips]
        self.clip = QComboBox(self)
        self.add_clips()
        self.clip.currentIndexChanged.connect(self.show_clip)
        self.layout.addWidget(self.clip)
        self.display = QWebView(self)
        self.layout.addWidget(self.display)

        self.button_box = QHBoxLayout()

        self.add_category_button = QPushButton("&Add category", self)
        self.add_category_button.clicked.connect(self.add_category)
        self.button_box.addWidget(self.add_category_button)

        self.button_box.addStretch(1)

        self.delete_button = QPushButton("&Delete", self)
        self.delete_button.clicked.connect(self.delete)
        self.button_box.addWidget(self.delete_button)

        self.move_button = QPushButton("&Recategorize", self)
        self.move_button.clicked.connect(self.recategorize)
        self.button_box.addWidget(self.move_button)

        self.layout.addLayout(self.button_box)

        self.show_clip()

    def add_category(self):
        new_category, ok = QInputDialog.getText(self, "Add Category", "Category:")
        if ok:
            self.manager.add_category(new_category)
            self.manager_ui.add_category(new_category)

    def add_clips(self):
        self.clip.clear()
        self.keys = [clip.title for clip in self.clips]
        self.clip.addItems(self.keys)

    def selected(self):
        return [clip for clip in self.clips
                   if clip.title ==
                self.keys[self.clip.currentIndex()]][0]
    def show_clip(self):
        try:
            self.display.setHtml(self.selected().html)
        except IndexError:
            pass

    def delete(self):
        self.clips.remove(self.selected())
        save_to_file("clips.brc", self.manager)
        self.add_clips()

    def recategorize(self):
        category, ok = QInputDialog.getItem(None, "Recategorize", "New category:", self.manager.categories.keys())
        self.manager.move(self.selected(), self.category, category)
        save_to_file("clips.brc", self.manager)
        self.manager_ui.refresh_viewers()

class ClipManagerViewer(QDialog):
    def __init__(self, manager):
        QDialog.__init__(self)
        self.setMinimumSize(500, 300)
        self.setModal(True)
        self.setWindowTitle("Clip Viewer")
        self.manager = manager
        self.set_up_ui()

    def set_up_ui(self):
        self.setLayout(None)
        self.layout = QFormLayout(self)
        self.tabs = QTabWidget()
        self.layout.addRow(self.tabs)
        self.clip_viewers = [ClipListViewer(category,
                                            self.manager.categories[category],
                                            self.manager,
                                            self,
                                            self)
                             for category in self.manager.categories.keys()]
        for viewer in self.clip_viewers:
            self.tabs.addTab(viewer, viewer.category)
        self.setLayout(self.layout)

    def add_category(self, category):
        viewer = ClipListViewer(category,
                                self.manager.categories[category],
                                self.manager,
                                self,
                                self)
        self.clip_viewers.append(viewer)
        self.tabs.addTab(viewer, viewer.category)

    def refresh_viewers(self):
        for viewer in self.clip_viewers:
            viewer.add_clips()

    def run(self):
        self.show()

    def delete(self):
        category = self.manager.categories.keys()[self.tabs.currentIndex()]
        self.manager.delete(self.current_clip, category)
        self.set_up_ui()

class ClipFiler(QDialog):
    def __init__(self, categories, parent=None):
        QDialog.__init__(self, parent)
        self.setModal(True)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.category = QComboBox(self)
        self.category.addItems(categories)

        self.layout.addRow("&Category:", self.category)

        self.title = QLineEdit(self)
        self.layout.addRow("&Title:", self.title)

        self.button_box = QHBoxLayout()
        self.button_box.addStretch(1)

        self.ok = QPushButton("&OK", self)
        self.ok.clicked.connect(self.ok_clicked)

        self.button_box.addWidget(self.ok)
    def run(self, callback):
        self.callback = callback
        self.show()
    def ok_clicked(self):
        self.hide()
        self.callback()

class BibleReader(QMainWindow, BibleReaderModel):
    """The main UI for the bible reader app"""

    def __init__(self):
        QMainWindow.__init__(self)
        BibleReaderModel.__init__(self)

        self.setWindowTitle(app_name)

        # add the main scripture display widget
        self.display = QWebView(self)
        self.display.setMinimumSize(600, 400)

        # it's all that's contained in this main window
        self.setCentralWidget(self.display)

        # the passage selection menu
        self.passage_menu = self.menuBar().addMenu("&Passage")

        self.set_up_passage_menu()

        # menu to select bible versions
        self.version_menu = self.menuBar().addMenu("&Version")

        self.set_up_version_menu()

        # add a menu for managing clips and set it up
        self.clip_menu = self.menuBar().addMenu("&Clips")
        self.set_up_clip_menu()

        self.view_menu = self.menuBar().addMenu("Vie&w")
        self.set_up_view_menu()

        self.lookup(self.last_passage)

    def set_up_passage_menu(self):
        # menu option to look up a passage
        lookup_action = QAction("&Look up", self)
        lookup_action.setShortcut("Ctrl+L")
        lookup_action.triggered.connect(self.interactive_lookup)

        # add it to the passage menu
        self.passage_menu.addAction(lookup_action)

        # menu option to browse for a passage
        browse_action = QAction("&Browse", self)
        browse_action.setShortcut("Ctrl+B")
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

    def set_up_version_menu(self):
        # return a callback for the version
        def make_callback(version):
            def cb():
                self.version = version
                self.lookup(self.last_passage)

            return cb

        # loop through the versions, adding them to the version menu
        for version in self.versions:
            action = QAction("&%s" % version.upper(), self)
            action.setShortcut("Ctrl+%s" % version.upper()[0])
            action.triggered.connect(make_callback(version))
            self.version_menu.addAction(action)

    def set_up_clip_menu(self):
        """Add choices to the clip menu"""
        # clear any existing choices
        self.clip_menu.clear()
        # add an option to add clips
        self.add_clip_action = QAction("Clip &selection", self)
        self.add_clip_action.triggered.connect(self.interactive_add_clip)
        self.clip_menu.addAction(self.add_clip_action)

        # add the submenus for each category
        self.add_clip_menus()

        view_action = QAction("&View", self)
        view_action.triggered.connect(self.view_clips)
        self.clip_menu.addAction(view_action)

    def view_clips(self):
        global viewer
        viewer = ClipManagerViewer(self.clip_manager)
        viewer.run()

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
    def interactive_add_clip(self):
        cf = ClipFiler(self.clip_manager.categories.keys())

        def cb():
            html = self.display.selectedHtml()
            self.add_clip(cf.title.text(), html)
            self.set_up_clip_menu()

        cf.run(cb)

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

    def lookup(self, passage_ref):
        self.display.setHtml(self.get_html(passage_ref))

    def add_clip_menus(self):
        for category in self.clip_manager.categories.keys():
            menu = self.clip_menu.addMenu(category)
            for clip in self.clip_manager.categories[category]:
                clip_action = menu.addAction(clip.title)

                def clip_handler(c):
                    def handler():
                        self.display.setHtml(c.html)

                    return handler

                clip_action.triggered.connect(clip_handler(clip))

reader = BibleReader()
reader.showMaximized()
app.exec_()
