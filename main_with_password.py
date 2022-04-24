import os
import sys
from PySide6.QtWidgets import QDialog, QApplication, QMessageBox
from PySide6.QtCore import QThread, Signal
from main import MyApp
from auth_ui_lower import Ui_Dialog
from auth import insert_log_data, is_valid_user_lower, update_time


class AuthenticationDialog(QDialog):
    def __init__(self):
        super(AuthenticationDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Authenticating")
        self.thread = None
        self.main_app = MyApp(self)
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.try_again_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.auth_page))
        self.ui.stackedWidget.setCurrentWidget(self.ui.auth_page)

    def login(self):
        email = self.ui.email_input.text().strip()
        password = self.ui.password_input.text()
        if len(email) > 4 and len(password) > 3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.notice_page)
            self.thread = AuthThread(email, password)
            self.thread.auth_complete.connect(self.auth_check)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            QMessageBox.warning(self, 'Invalid Login', 'Please enter valid information.')

    def auth_check(self, auth_success):
        if auth_success:
            self.accept()
            self.main_app.show()
            self.thread.deleteLater()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.failed_auth_page)
            self.ui.stackedWidget.setCurrentWidget(self.ui.failed_auth_page)


class AuthThread(QThread):
    auth_complete = Signal(bool)
    finished = Signal()

    def __init__(self, email, password):
        super(AuthThread, self).__init__()
        self.email = email
        self.password = password

    def run(self):
        is_done, item_key = is_valid_user_lower(self.email, self.password)
        if is_done:
            update_time('usersv5', item_key)
        else:
            insert_log_data()
        self.auth_complete.emit(is_done)
        self.finished.emit()


if __name__ == '__main__':
    application_path = None
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(os.path.abspath(sys.executable))
    elif __file__:
        application_path = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    window = AuthenticationDialog()
    window.show()
    sys.exit(app.exec())