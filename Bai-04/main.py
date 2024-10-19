from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QMessageBox
import sys
from PyQt6 import uic 
import os

class LoginWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "UI\\login.ui")
        uic.loadUi(ui_path, self)

        self.button = self.findChild(QPushButton, 'pushButtonLogin')  
        self.text_edit = self.findChild(QTextEdit, 'textEditUsername')   

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.show_popup("Clicked!")

        # text = self.text_edit.toPlainText()

        # self.text_edit.setPlainText("Button clicked!")

    def show_popup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText("Nội dung của thông báo: " +  message)
        msg.setIcon(QMessageBox.Icon.Information)
        
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
app.exec()
