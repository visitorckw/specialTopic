import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainwindow import *
from create_accountwindow import *
from login_window import *
from PyQt5.QtWidgets import  QMessageBox


class loginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.creat_account)
        self.ui.pushButton_2.clicked.connect(self.login)
        self.ui.pushButton_3.clicked.connect(self.delete)

    def login(self):
        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        print("account : "+account )
        print("password : "+password)
        window.hide()
        mainwindow.show()

    def creat_account(self):
        window.hide()
        accountWindow.show()

    def delete(self):          # 清除
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()




class create_accountWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(create_accountWindow, self).__init__()
        self.ui = Ui_create_accountWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.confirm)
        self.ui.pushButton_2.clicked.connect(self.delete)
        self.ui.pushButton_3.clicked.connect(self.clear)

    def clear(self):          # 清除
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def confirm(self):          # 確認
        account = self.ui.lineEdit.text()
        password1 = self.ui.lineEdit_2.text()
        password2 = self.ui.lineEdit_3.text()
        if(password1 != password2):
            msg = QMessageBox()
            msg.setWindowTitle("錯誤提示")
            msg.setText("重新確認密碼")
            msg.exec_()
        else:
            self.close()
            window.show()
        print("account : " + account)
        print("password : " + password1)

    def delete(self):
        self.close()
        window.show()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.logout)

    def logout(self):
        flag = QtWidgets.QMessageBox.question(self, "登出","是否要登出")
        if flag == QtWidgets.QMessageBox.Yes:
            self.close()
            window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loginWindow()
    mainwindow = MainWindow()
    accountWindow = create_accountWindow()
    window.show()
    sys.exit(app.exec_())
