from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic 
import os

class Window1(QMainWindow):  
    def __init__(self):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "UI\\Window1.ui")
        uic.loadUi(ui_path, self)


app = QApplication(sys.argv)
window = Window1()
window.show()
app.exec()
