from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt6.QtCore import QSize
import sys
from PyQt6 import uic 
import os
from scripts.NoteItemScr import NoteItem
from scripts.AddNoteScr import AddNote

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


    def onPushButtonAdd(self):
        self.AddNoteWindow.show()


    def load_notes(self):
        self.listWidget.clear()
        self.listWidget.setSpacing(10)

        ds_note = self.database.get_notes()

        for note in ds_note:
            noteWidget = NoteItem(note)

            item = QListWidgetItem(self.listWidget)

            noteWidget.setFixedSize(500, 120)

            item.setSizeHint(QSize(500, 120))

            self.listWidget.addItem(item)
            
            self.listWidget.setItemWidget(item, noteWidget)




