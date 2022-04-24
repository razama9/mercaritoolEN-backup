# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_ui_lower.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(521, 152)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 10, 501, 131))
        self.auth_page = QWidget()
        self.auth_page.setObjectName(u"auth_page")
        self.email_input = QLineEdit(self.auth_page)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(150, 20, 280, 25))
        self.email_input.setClearButtonEnabled(True)
        self.label = QLabel(self.auth_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 24, 81, 17))
        self.login_btn = QPushButton(self.auth_page)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(200, 94, 89, 25))
        self.label_2 = QLabel(self.auth_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 54, 81, 17))
        self.password_input = QLineEdit(self.auth_page)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(150, 50, 280, 25))
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setClearButtonEnabled(True)
        self.stackedWidget.addWidget(self.auth_page)
        self.notice_page = QWidget()
        self.notice_page.setObjectName(u"notice_page")
        self.label_3 = QLabel(self.notice_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 16, 451, 91))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.notice_page)
        self.failed_auth_page = QWidget()
        self.failed_auth_page.setObjectName(u"failed_auth_page")
        self.label_4 = QLabel(self.failed_auth_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 451, 51))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.try_again_btn = QPushButton(self.failed_auth_page)
        self.try_again_btn.setObjectName(u"try_again_btn")
        self.try_again_btn.setGeometry(QRect(200, 70, 89, 25))
        self.stackedWidget.addWidget(self.failed_auth_page)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter email", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.login_btn.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter password", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Authenticating. Please wait...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Sorry! Authentication failed!", None))
        self.try_again_btn.setText(QCoreApplication.translate("Dialog", u"Try Again", None))
    # retranslateUi

