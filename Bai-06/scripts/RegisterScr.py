from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic 
import os

class Register(QMainWindow):  
    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Register.ui")
        uic.loadUi(ui_path, self)
