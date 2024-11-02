from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic 
import os

from scripts.LoginScr import Login
from scripts.RegisterScr import Register
from scripts.MainPageScr import MainPage
from models.database import Database


class AppController:
    def __init__(self):
        # Khởi tạo dữ liệu
        self.db = Database()

        # Khởi tạo các cửa sổ
        self.login_window = Login(self)
        self.register_window = Register(self)
        self.main_window = MainPage(self, self.db)

        
    def show_login_page(self):
        self.login_window.show()

    def show_register_page(self):
        self.register_window.show()        

    def show_main_page(self):
        self.main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = AppController()
    controller.show_login_page()
    app.exec()