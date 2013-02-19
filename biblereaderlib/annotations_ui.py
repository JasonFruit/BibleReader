from PySide.QtCore import *
from PySide.QtGui import *

from reference_parser import ReferenceParser

from annotations import Annotation, AnnotationManager
__author__ = 'jason'


class AnnotationDialog(QDialog):
    def __init__(self, annotation, parent=None):
        QDialog.__init__(self, parent)

        self.parser = ReferenceParser()

        self.annotation = annotation

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.form_layout = QFormLayout()

        self.reference_entry = QLineEdit(self)
        self.reference_entry.setText(unicode(self.annotation.reference))

        self.form_layout.addRow("Reference:", self.reference_entry)

        self.text_entry = QTextEdit(self)
        self.text_entry.setText(self.annotation.text)

        self.form_layout.addRow(QLabel("Notes:"))
        self.form_layout.addRow(self.text_entry)

        self.layout.addLayout(self.form_layout)

        self.button_box = QHBoxLayout()

        self.button_box.addStretch()

        self.ok_button = QPushButton("&OK")
        self.ok_button.clicked.connect(self.okay)

        self.button_box.addWidget(self.ok_button)

        self.layout.addLayout(self.button_box)

    def okay(self):
        self.annotation.reference = self.parser.parse(
            self.reference_entry.text())
        self.annotation.text = self.text_entry.toPlainText()
        self.accepted.emit()
        self.close()

class AnnotationList(QListWidget):
    annotation_changed = Signal(Annotation)
    def __init__(self, category, annotations, parent=None):
        QListWidget.__init__(self, parent)
        self.category = category
        self.annotations = annotations
        self.annotations.sort()

        for annotation in self.annotations:
            item = QListWidgetItem(unicode(annotation.reference),
                                   self)
            item.setData(Qt.UserRole, annotation)

        self.currentItemChanged.connect(self.on_changed)

    def on_changed(self):
        self.annotation_changed.emit(self.currentItem().data(Qt.UserRole))

class CategoryViewer(QWidget):
    def __init__(self, category, annotations, parent=None):
        QWidget.__init__(self, parent)

        self.category = category
        self.annotations = annotations

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.annotation_text = QPlainTextEdit(self)

        self.annotation_text.textChanged.connect(self.on_text_changed)

        self.annotation_list = AnnotationList(self.category,
                                              self.annotations,
                                              self)

        self.annotation_list.annotation_changed.connect(self.show_annotation)

        self.layout.addWidget(self.annotation_list, stretch=0)
        self.layout.addWidget(self.annotation_text, stretch=1)
        self.setLayout(self.layout)

    def current_annotation(self):
        return self.annotation_list.currentItem().data(Qt.UserRole)

    def show_annotation(self, annotation):
        self.annotation_text.setPlainText(annotation.text)

    def on_text_changed(self):
        self.current_annotation().text = self.annotation_text.toPlainText()


class AnnotationsDialog(QDialog):
    def __init__(self, manager, parent=None):
        QDialog.__init__(self, parent)
        self.manager = manager

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.tabs = QTabWidget(self)

        for category in manager.keys():
            self.tabs.addTab(CategoryViewer(category,
                                            manager[category],
                                            self),
                             category)

        self.layout.addWidget(self.tabs)
