from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt6 import uic 
import os
from scripts.MainPageScr import MainPage
from scripts.RegisterScr import Register

class Login(QMainWindow):  
    def __init__(self):
        super().__init__()
        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Login.ui")
        uic.loadUi(ui_path, self)

        # Kết nối nút đăng nhập với hàm đăng nhập 
        self.pushButtonDangNhap.clicked.connect(self.onPushButtonDangNhap)

        # Tạo trang chính 
        self.main_page = None

        # Kết nôi nút đăng kí tài khoản với hàm đăng kí tài khoản 
        self.pushButtonDangKi.clicked.connect(self.onPushButtonDangKi)
        # Tạo đối tượng trang đăng kí 
        self.registerPage = None

    def onPushButtonDangNhap(self):
        # Nếu tài khoản và mật khẩu đúng thì thực hiện đăng nhập 
        if self.textEditTaiKhoan.toPlainText() == "admin123" and self.textEditMatKhau.toPlainText() == "123":
            self.main_page = MainPage()
            self.main_page.show()
            self.hide()
        else: 
            msgBox = QMessageBox()
            msgBox.setText("Tài khoản hoặc mật khẩu không hợp lệ!")
            msgBox.exec()

    def onPushButtonDangKi(self):
        self.registerPage = Register(self)
        self.registerPage.show()
        self.hide()


