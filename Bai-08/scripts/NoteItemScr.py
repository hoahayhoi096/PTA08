from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import os

class NoteItem(QWidget):
    def __init__(self, note, parent=None):
        super(NoteItem, self).__init__(parent)

        ui_path = os.path.join(os.path.dirname(__file__), "../UI/NoteItem.ui")
        uic.loadUi(ui_path, self)

        self.labelTitle.setText(note.title)
        self.labelContent.setText(note.content)
