from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt6 import uic 
import os

class Login(QMainWindow):  
    def __init__(self, controller):
        super().__init__()
        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Login.ui")
        uic.loadUi(ui_path, self)

        # Tạo đối tượng controller để điều hướng các trang 
        self.controller = controller

        # Kết nối nút đăng nhập với hàm đăng nhập 
        self.pushButtonDangNhap.clicked.connect(self.onPushButtonDangNhap)

        # Kết nôi nút đăng kí tài khoản với hàm đăng kí tài khoản 
        self.pushButtonDangKi.clicked.connect(self.onPushButtonDangKi)


    def onPushButtonDangNhap(self):
        # Nếu tài khoản và mật khẩu đúng thì thực hiện đăng nhập 
        if self.textEditTaiKhoan.toPlainText() == "admin123" and self.textEditMatKhau.toPlainText() == "123":
            self.controller.show_main_page()
            self.close()
        else: 
            msgBox = QMessageBox()
            msgBox.setText("Tài khoản hoặc mật khẩu không hợp lệ!")
            msgBox.exec()



    def onPushButtonDangKi(self):
        self.controller.show_login_page()
        self.hide()


