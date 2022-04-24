import os
import sys
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import QThread, Signal
from main import MyApp
from auth_ui import Ui_Dialog
from auth import insert_log_data, is_valid_user_higher, update_time
from getmac import get_mac_address as gma


class AuthenticationDialog(QDialog):
    def __init__(self):
        super(AuthenticationDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Authenticating")
        self.main_app = MyApp(self)
        self.thread = AuthThread()
        self.thread.auth_complete.connect(self.auth_check)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def auth_check(self, auth_success):
        if auth_success:
            self.accept()
            self.main_app.show()
            self.thread.deleteLater()
        else:
            self.ui.label.setText("You're not authenticated!")


class AuthThread(QThread):
    auth_complete = Signal(bool)
    finished = Signal()

    def run(self):
        mac_address = gma()
        is_done, item_key = is_valid_user_higher(mac_address)
        if is_done:
            update_time("usersv4", item_key)
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
    # window = MyApp()
    window = AuthenticationDialog()
    window.show()
    sys.exit(app.exec())