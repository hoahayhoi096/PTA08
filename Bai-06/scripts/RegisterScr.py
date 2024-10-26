from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic 
import os

class Register(QMainWindow):  
    def __init__(self , loginPage):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Register.ui")
        uic.loadUi(ui_path, self)

        self.pushButtonQuayLai.clicked.connect(self.onPushButtonQuayLai)
        self.loginPage = loginPage

    def onPushButtonQuayLai(self):
        self.loginPage.show()
        self.hide()



