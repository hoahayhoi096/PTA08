from PyQt6.QtWidgets import QDialog, QMessageBox, QPushButton
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

        self.btnDong.clicked.connect(self.onButtonDongClicked)
        self.btnLuu.clicked.connect(self.onButtonLuuClicked)



    def set_note_data(self):
        self.lineEditTitle.setText(self.note.title)
        self.textEditContent.setText(self.note.content)

    def onButtonDongClicked(self):
        self.close()

    def onButtonLuuClicked(self):
        title = self.lineEditTitle.text()
        content = self.textEditContent.toPlainText()

        self.note.title = title
        self.note.content = content

        self.database.update_note(self.note)

        self.controller.main_window.load_notes()
        QMessageBox.information(self, "Thông báo", "Cập nhật ghi chú thành công!")

