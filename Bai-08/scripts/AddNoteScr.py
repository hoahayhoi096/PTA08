from PyQt6.QtWidgets import QDialog
from PyQt6 import uic
import os
from models.note import Note

class AddNote(QDialog):
    def __init__(self, parent = None,  database = None, controller = None):
        super(AddNote, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/AddNote.ui")
        uic.loadUi(ui_path, self)

        self.database = database 
        self.controller = controller
        self.pushButtonDong.clicked.connect(self.onPushButtonDong)
        self.pushButtonThem.clicked.connect(self.onPushButtonThem)

    def onPushButtonThem(self):
        title = self.textEditTitle.toPlainText()
        content = self.plainTextEditContent.toPlainText()
        if title and content:
            new_note = Note(title, content)
            self.database.add_note(new_note)
            self.controller.main_window.load_notes()
            self.clear_all_text()


    def onPushButtonDong(self):
        self.close()

    def clear_all_text(self):
        self.textEditTitle.setPlainText("")
        self.plainTextEditContent.setPlainText("")



