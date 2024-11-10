from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt6.QtCore import QSize, Qt
import sys
from PyQt6 import uic 
import os
from scripts.NoteItemScr import NoteItem
from scripts.AddNoteScr import AddNote
from scripts.NoteDetailScr import NoteDetail

class MainPage(QMainWindow):  
    def __init__(self, controller, database):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "../UI/MainPage.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        self.database = database

        self.load_notes()
        self.AddNoteWindow = AddNote(None, self.database, self.controller)
        self.pushButtonAdd.clicked.connect(self.onPushButtonAdd)

        self.listWidget.itemClicked.connect(self.onItemClicked)

        self.NoteDetailWindow = None


    def onItemClicked(self, item):
        # Lấy id của note từ Item trong list các note
        note_id = item.data(Qt.ItemDataRole.UserRole)
        # Tìm note trong database dựa vào id vừa có 
        note = self.database.get_note_by_id(note_id)

        # Nếu note được tìm thấy (có tồn tại trong database)
        if note:
            # Hiển thị thông tin của note lên giao diện 
            self.NoteDetailWindow = NoteDetail(None, self.controller, self.database, note)
            self.NoteDetailWindow.show()


    def onPushButtonAdd(self):
        self.AddNoteWindow.show()


    def load_notes(self):
        self.listWidget.clear()
        self.listWidget.setSpacing(10)

        ds_note = self.database.get_notes()

        for note in ds_note:
            noteWidget = NoteItem(note)

            item = QListWidgetItem(self.listWidget)

            # Gán id của note vào item với nơi lưu trữ là Qt.UserRole 
            item.setData(Qt.ItemDataRole.UserRole, note.id)

            noteWidget.setFixedSize(500, 120)

            item.setSizeHint(QSize(500, 120))

            self.listWidget.addItem(item)
            
            self.listWidget.setItemWidget(item, noteWidget)




