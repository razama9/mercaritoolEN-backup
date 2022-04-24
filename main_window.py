# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.select_all_btn = QPushButton(self.centralwidget)
        self.select_all_btn.setObjectName(u"select_all_btn")
        self.select_all_btn.setEnabled(False)
        self.select_all_btn.setGeometry(QRect(10, 20, 81, 25))
        self.deselect_all_btn = QPushButton(self.centralwidget)
        self.deselect_all_btn.setObjectName(u"deselect_all_btn")
        self.deselect_all_btn.setEnabled(False)
        self.deselect_all_btn.setGeometry(QRect(110, 20, 101, 25))
        self.import_btn = QPushButton(self.centralwidget)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setEnabled(False)
        self.import_btn.setGeometry(QRect(709, 20, 141, 25))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 420, 181, 20))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.unit_radio_btn = QRadioButton(self.centralwidget)
        self.unit_radio_btn.setObjectName(u"unit_radio_btn")
        self.unit_radio_btn.setGeometry(QRect(60, 460, 191, 23))
        self.unit_radio_btn.setChecked(True)
        self.percent_radio_btn = QRadioButton(self.centralwidget)
        self.percent_radio_btn.setObjectName(u"percent_radio_btn")
        self.percent_radio_btn.setGeometry(QRect(260, 460, 191, 23))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 420, 16, 171))
        self.line.setStyleSheet(u"Line {\n"
"	\n"
"   color: #7f8c8d\n"
"}")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.reduction_amount = QLineEdit(self.centralwidget)
        self.reduction_amount.setObjectName(u"reduction_amount")
        self.reduction_amount.setGeometry(QRect(460, 460, 113, 25))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 501, 181, 20))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.list_lower_val = QSpinBox(self.centralwidget)
        self.list_lower_val.setObjectName(u"list_lower_val")
        self.list_lower_val.setGeometry(QRect(210, 499, 70, 26))
        self.list_lower_val.setAlignment(Qt.AlignCenter)
        self.list_lower_val.setMaximum(1000000000)
        self.list_upper_val = QSpinBox(self.centralwidget)
        self.list_upper_val.setObjectName(u"list_upper_val")
        self.list_upper_val.setGeometry(QRect(320, 499, 70, 26))
        self.list_upper_val.setAlignment(Qt.AlignCenter)
        self.list_upper_val.setMaximum(1000000000)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 501, 21, 20))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 501, 61, 20))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.reduction_btn = QPushButton(self.centralwidget)
        self.reduction_btn.setObjectName(u"reduction_btn")
        self.reduction_btn.setEnabled(False)
        self.reduction_btn.setGeometry(QRect(248, 550, 141, 25))
        self.website_url = QLabel(self.centralwidget)
        self.website_url.setObjectName(u"website_url")
        self.website_url.setGeometry(QRect(657, 560, 181, 20))
        self.website_url.setStyleSheet(u"color: rgb(52, 101, 164);")
        self.website_url.setAlignment(Qt.AlignCenter)
        self.website_url.setOpenExternalLinks(True)
        self.website_url.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.qr_code_label = QLabel(self.centralwidget)
        self.qr_code_label.setObjectName(u"qr_code_label")
        self.qr_code_label.setGeometry(QRect(665, 430, 161, 121))
        self.qr_code_label.setAlignment(Qt.AlignCenter)
        self.start_browser_btn = QPushButton(self.centralwidget)
        self.start_browser_btn.setObjectName(u"start_browser_btn")
        self.start_browser_btn.setGeometry(QRect(130, 651, 131, 25))
        self.quit_browser_btn = QPushButton(self.centralwidget)
        self.quit_browser_btn.setObjectName(u"quit_browser_btn")
        self.quit_browser_btn.setEnabled(False)
        self.quit_browser_btn.setGeometry(QRect(355, 651, 131, 25))
        self.login_btn = QPushButton(self.centralwidget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setEnabled(False)
        self.login_btn.setGeometry(QRect(580, 651, 131, 25))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 600, 681, 91))
        self.frame.setStyleSheet(u"QFrame {border-width: 1;\n"
"                                border-radius: 3;\n"
"                                border-style: solid;\n"
"                                border-color: #7f8c8d}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 615, 181, 20))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(36, 452, 581, 40))
        self.frame_2.setStyleSheet(u"QFrame {border-width: 1;\n"
"                                border-radius: 3;\n"
"                                border-style: solid;\n"
"                                border-color: #7f8c8d}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(36, 491, 581, 40))
        self.frame_3.setStyleSheet(u"QFrame {border-width: 1;\n"
"                                border-radius: 3;\n"
"                                border-style: solid;\n"
"                                border-color: #7f8c8d}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(12, 55, 840, 351))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(165)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.same_action_check = QCheckBox(self.centralwidget)
        self.same_action_check.setObjectName(u"same_action_check")
        self.same_action_check.setGeometry(QRect(350, 21, 201, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame.raise_()
        self.select_all_btn.raise_()
        self.deselect_all_btn.raise_()
        self.import_btn.raise_()
        self.label_2.raise_()
        self.unit_radio_btn.raise_()
        self.percent_radio_btn.raise_()
        self.line.raise_()
        self.reduction_amount.raise_()
        self.label_3.raise_()
        self.list_lower_val.raise_()
        self.list_upper_val.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.reduction_btn.raise_()
        self.website_url.raise_()
        self.qr_code_label.raise_()
        self.start_browser_btn.raise_()
        self.quit_browser_btn.raise_()
        self.login_btn.raise_()
        self.label_7.raise_()
        self.tableWidget.raise_()
        self.same_action_check.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.select_all_btn.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.deselect_all_btn.setText(QCoreApplication.translate("MainWindow", u"Deselect All", None))
        self.import_btn.setText(QCoreApplication.translate("MainWindow", u"Import Products", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bulk price settings", None))
        self.unit_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Unit price specification", None))
        self.percent_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Percent specification", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time Interval", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"seconds", None))
        self.reduction_btn.setText(QCoreApplication.translate("MainWindow", u"Update Products", None))
        self.website_url.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://info.accestrade.net\"><span style=\" color:#0000ff;\">info.accestrade.net</span></a></p></body></html>", None))
        self.qr_code_label.setText(QCoreApplication.translate("MainWindow", u"QR Code", None))
        self.start_browser_btn.setText(QCoreApplication.translate("MainWindow", u"Start Browser", None))
        self.quit_browser_btn.setText(QCoreApplication.translate("MainWindow", u"Quit Browser", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Control Buttons", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.same_action_check.setText(QCoreApplication.translate("MainWindow", u"Same action to all items", None))
    # retranslateUi

