from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
import os

class NoteDetail(QDialog):
    def __init__(self,  parent=None, controller = None, database=None, note = None):
        super().__init__(parent)

        self.setWindowTitle("Note Details")

        ui_path = os.path.join(os.path.dirname(__file__), "../UI/NoteDetail.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        self.database = database
        self.note = note

        self.set_note_data()


    def set_note_data(self):
        self.lineEditTitle.setText(self.note.title)
        self.textEditContent.setText(self.note.content)
