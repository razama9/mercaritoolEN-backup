import os
import platform
import sys
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QMessageBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QComboBox
)
from PySide6.QtGui import QPixmap, QIcon, QColor
from PySide6.QtCore import QThread, Signal, Qt
from main_window import Ui_MainWindow
from mercari_web import *
import webbrowser
import rc_files


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Mercari Automation')
        self.setWindowIcon(QIcon(":/icon.png"))
        qr_pixmap = QPixmap(":/qrcode.jpeg")
        self.ui.qr_code_label.setPixmap(qr_pixmap)
        self.thread = None
        self.driver = None
        self.all_listings = []
        self.username = None
        self.password = None
        self.percentage = 10
        self.unit_value = 100
        self.ui.reduction_amount.setText(str(self.unit_value))
        self.ui.unit_radio_btn.toggled.connect(self.handle_radio_btn_changes)
        self.ui.list_lower_val.setValue(600)
        self.ui.list_upper_val.setValue(1800)
        self.listing_actions = [
            'Do nothing or Select an action (default)',
            'Only decrease price',
            'Display on top',
            'Only increase price',
            'Private'
        ]
        self.draft_actions = [
            'Do nothing or Select an action (default)',
            'Publish The Product'
        ]
        self.ui.start_browser_btn.clicked.connect(self.open_browser)
        self.ui.quit_browser_btn.clicked.connect(self.quit_browser)
        self.ui.reduction_btn.clicked.connect(self.decrease_prices)
        self.header_sizes = [300, 100, 150, 150, 50]
        for i, s in enumerate(self.header_sizes):
            self.ui.tableWidget.setColumnWidth(i, s)
        self.action_column = 2
        self.ui.tableWidget.itemClicked.connect(self.open_product_in_browser)
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.same_action_check.stateChanged.connect(lambda: self.action_manager(0))
        self.ui.import_btn.clicked.connect(self.get_listings)
        self.ui.login_btn.clicked.connect(self.make_manual_login)
        self.ui.deselect_all_btn.clicked.connect(lambda: self.select_all_products(False))
        self.ui.select_all_btn.clicked.connect(lambda: self.select_all_products())

    def handle_radio_btn_changes(self):
        old_value = self.ui.reduction_amount.text()
        if self.ui.unit_radio_btn.isChecked():
            self.percentage = int(old_value)
            self.ui.reduction_amount.setText(str(self.unit_value))
        else:
            self.unit_value = int(old_value)
            self.ui.reduction_amount.setText(str(self.percentage))

    def closeEvent(self, event):
        if self.driver:
            close = QMessageBox.question(
                self,
                "Quit?",
                "Are you sure you want to close the app?",
                QMessageBox.Yes | QMessageBox.No
            )
            if close == QMessageBox.Yes:
                if self.driver:
                    self.quit_browser()
                event.accept()
            else:
                event.ignore()
        else:
            pass

    def make_manual_login(self):
        QMessageBox.information(self, 'Manual Login', "Please login manually on the browser")

    def action_manager(self, t_index):
        same_to_all = self.ui.same_action_check.isChecked()
        if same_to_all:
            for i in range(len(self.all_listings)):
                if self.all_listings[i]['source'] == 'listings':
                    self.ui.tableWidget.cellWidget(i, self.action_column).setCurrentIndex(t_index)

    def open_product_in_browser(self, item):
        if item.column() == 3:
            item_text = item.text().strip()
            if item_text != '':
                s_url = f"https://jp.mercari.com/item/{item_text}"
                webbrowser.open(s_url)

    def decrease_prices(self):
        interval_from = self.ui.list_lower_val.value()
        interval_to = self.ui.list_upper_val.value()
        if interval_from > 0 and interval_to > 0 and interval_to > interval_from:
            self.update_dialog = UpdateDialog(self)
            self.update_dialog.setWindowTitle("Updating listings...")
            self.update_dialog.resize(350, 150)
            self.msg_label = QLabel()
            self.error_label = QLabel()
            self.error_label.setStyleSheet('QLabel {color: #cc0000;}')
            self.ok_btn = QPushButton("Yes")
            self.ok_btn.clicked.connect(self.update_dialog.accept)
            self.ok_btn.setVisible(False)
            lay = QVBoxLayout()
            lay.addWidget(self.msg_label, alignment=Qt.AlignHCenter)
            lay.addWidget(self.error_label, alignment=Qt.AlignHCenter)
            lay.addWidget(self.ok_btn)
            self.update_dialog.setLayout(lay)
            self.update_dialog.setModal(True)
            self.update_dialog.show()
            self.marked_items = 0
            for i in range(self.ui.tableWidget.rowCount()):
                if self.ui.tableWidget.item(i,0).checkState() == Qt.Checked:
                    self.all_listings[i]['marked'] = True
                    self.all_listings[i]['action'] = self.ui.tableWidget.cellWidget(i, self.action_column).currentIndex()
                    self.marked_items += 1
            if self.ui.percent_radio_btn.isChecked():
                is_percent = True
                if self.ui.reduction_amount.text().strip() != '':
                    self.percentage = int(self.ui.reduction_amount.text())
            else:
                is_percent = False
                if self.ui.reduction_amount.text().strip() != "":
                    self.unit_value = int(self.ui.reduction_amount.text())
            self.interval1 = [randint(interval_from, interval_to) for _ in range(self.marked_items)]
            self.msg_label.setText(f"Updating products 1 / {self.marked_items}")
            QApplication.processEvents()
            
            self.thread = ChangePrice(
                driver=self.driver,
                listings=self.all_listings,
                is_percent=is_percent,
                value=self.unit_value,
                percentage=self.percentage,
                interval=self.interval1,
                marked_items=self.marked_items
            )
            self.thread.progress.connect(self.update_loader)
            self.thread.decrease_complete.connect(self.decrease_completed)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            QMessageBox.warning(self, "Range Error", "Ranges can't be zero \
and right one should be greater than left one")

    def decrease_completed(self, updated_listings):
        self.msg_label.setText("Completed!")
        self.ok_btn.setVisible(True)
        self.update_listings(updated_listings)

    def update_loader(self, updt):
        i, is_successful = updt
        self.msg_label.setText(f"Updating products {i} / {self.marked_items}")
        # time_now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        # self.ui.last_update_time.setText(f"{time_now}")
        QApplication.processEvents()
        sleep(1)
        if is_successful:
            self.error_label.setText("")
        else:
            self.error_label.setText(f"Price could not be updated for row {i+1}")

    def button_manager(self, select_btn=None, import_btn=None, reduction_btn=None, start_btn=None, quit_btn=None, login_btn=None):
        if select_btn is not None:
            self.ui.select_all_btn.setEnabled(select_btn)
            self.ui.deselect_all_btn.setEnabled(select_btn)
        if import_btn is not None:
            self.ui.import_btn.setEnabled(import_btn)
        if reduction_btn is not None:
            self.ui.reduction_btn.setEnabled(reduction_btn)
        if start_btn is not None:
            self.ui.start_browser_btn.setEnabled(start_btn)
        if quit_btn is not None:
            self.ui.quit_browser_btn.setEnabled(quit_btn)
        if login_btn is not None:
            self.ui.login_btn.setEnabled(login_btn)

    def get_listings(self):
        if self.driver:
            self.button_manager(import_btn=False, reduction_btn=False, quit_btn=False)
            self.update_dialog3 = UpdateDialog(self)
            self.update_dialog3.setWindowTitle("Loading products")
            self.update_dialog3.resize(350, 150)
            self.msg_label3 = QLabel("Loading the products.\nThis will take a while.\nPlease wait a moment...")
            self.ok_btn3 = QPushButton("Close")
            self.ok_btn3.clicked.connect(self.update_dialog3.accept)
            self.ok_btn3.setVisible(False)
            lay3 = QVBoxLayout()
            lay3.addWidget(self.msg_label3, alignment=Qt.AlignHCenter)
            lay3.addWidget(self.ok_btn3)
            self.update_dialog3.setLayout(lay3)
            self.update_dialog3.setModal(True)
            self.update_dialog3.show()
            QApplication.processEvents()
            self.thread = GetListings(self.driver)
            self.thread.complete_signal.connect(self.update_listings)
            self.thread.login_signal.connect(lambda: QMessageBox.warning(self, 'Please try again', 'Please check if you\'re logged in and then try again!'))
            self.thread.finished.connect(self.complete_get_listings)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()

    def complete_get_listings(self):
        self.button_manager(select_btn=True, import_btn=True, quit_btn=True, reduction_btn=True)

    def update_listings(self, n_listings):
        if len(n_listings) > 0:
            self.msg_label3.setText("All items are loaded!")
        else:
            self.msg_label3.setText("No items are loaded! Please try again.")
        self.ok_btn3.setVisible(True)
        self.all_listings = n_listings
        self.show_listings()

    def select_all_products(self, select=True):
        for i in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.item(i, 0).setCheckState(Qt.Checked if select else Qt.Unchecked)

    def remove_listings(self):
        self.ui.tableWidget.setRowCount(0)

    def show_listings(self):
        self.button_manager(select_btn=True)
        self.ui.tableWidget.setRowCount(0)
        for index, listing in enumerate(self.all_listings):
            self.ui.tableWidget.insertRow(index)
            # Title
            title = QTableWidgetItem(listing['title'])
            if listing['source']:
                title.setCheckState(Qt.Unchecked)
                title.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            else:
                title.setFlags(Qt.ItemIsEnabled)
            # Status
            if listing['status'] is None:
                status = 'Untouched'
            elif listing['status'] is False:
                status = 'Error'
            else:
                status = listing['status']
            # Product ID
            product_url = listing['url']
            product_id = product_url.split('/')[-1]
            product_table_item = QTableWidgetItem(product_id)
            product_table_item.setToolTip("Click on the Product ID to open the product link")
            
            row_items = [
                (title, 300, False),
                (QTableWidgetItem(listing['price']), 100, True),
                (QTableWidgetItem(), 150, True),
                (product_table_item, 150, True),
                (QTableWidgetItem(status), 50, True)
            ]
            for j in range(len(row_items)):
                s_item = row_items[j][0]
                if row_items[j][2]:
                    s_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.ui.tableWidget.setItem(index, j, s_item)
                self.ui.tableWidget.setColumnWidth(j, row_items[j][1])
            
            # Action Options
            if listing['source'] == 'listings':
                combo_box_items = self.listing_actions
            elif listing['source'] == 'drafts' or listing['source'] == 'unpublished':
                combo_box_items = self.draft_actions
            else:
                combo_box_items = None
            if combo_box_items:
                action_options = ActionOptions(parent=self, box_items=combo_box_items, product_serial=index)
                self.ui.tableWidget.setCellWidget(index, 2, action_options)
                self.ui.tableWidget.cellWidget(index, self.action_column).setCurrentIndex(listing['action'])

    def open_browser(self):
        if not self.driver:
            self.button_manager(start_btn=False)
            self.thread = OpenChrome()
            self.thread.start()
            self.thread.browser_signal.connect(self.update_browser_instance)

    def update_browser_instance(self, driver):
        self.driver = driver
        self.button_manager(quit_btn=True, import_btn=True, login_btn=True)

    def quit_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.button_manager(start_btn=True, quit_btn=False, select_btn=False, import_btn=False, reduction_btn=False, login_btn=False)
            self.remove_listings()


class ActionOptions(QComboBox):
    def __init__(self, box_items, product_serial, parent=None):
        super(ActionOptions, self).__init__(parent)
        self.parent = parent
        self.addItems(box_items)
        if self.parent.all_listings[product_serial]['source'] == 'listings':
            self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        current_index = self.currentIndex()
        self.parent.action_manager(current_index)


class ChangePrice(QThread):
    progress = Signal(tuple)
    decrease_complete = Signal(list)
    finished = Signal()

    def __init__(self, driver, listings, is_percent, value, percentage, interval, marked_items, parent=None):
        QThread.__init__(self, parent)
        self.driver = driver
        self.listings = listings
        self.is_percent = is_percent
        self.value = value
        self.percentage = percentage
        self.interval = interval
        self.marked_items = marked_items
        self.n = len(self.listings)

    def run(self):
        randomized_position = get_randomized_positions(len(self.listings))
        product_counter = 0
        for r in randomized_position:
            if self.listings[r]['marked'] and self.listings[r]['action'] != 0 and self.listings[r]['url']:
                try:
                    if self.is_percent:
                        inc_sign = '%'
                        amount = self.percentage
                    else:
                        inc_sign = ''
                        amount = self.value
                    if self.listings[r]['source'] == 'listings':
                        if self.listings[r]['action'] == 2:
                            # Display on top
                            self.driver.get(self.listings[r]['url'])
                            price = wfe_by_xpath(self.driver, '//mer-price[@data-testid="price"]').get_attribute('value')
                            sleep(1)
                            new_price = get_changed_price(price, by_percent=self.is_percent, unit_amount=self.value, percent_amount=self.percentage)
                            change_price(self.driver, new_price)
                            sleep(randint(6,10))
                            change_price(self.driver, price)
                            self.listings[r]['status'] = f"✓ -{amount}{inc_sign} → +{amount}{inc_sign}"
                        elif self.listings[r]['action'] == 1:
                            # Decrease Price
                            self.driver.get(self.listings[r]['url'])
                            price = wfe_by_xpath(self.driver, '//mer-price[@data-testid="price"]').get_attribute('value')
                            sleep(1)
                            new_price = get_changed_price(price, by_percent=self.is_percent, unit_amount=self.value, percent_amount=self.percentage)
                            change_price(self.driver, new_price)
                            self.listings[r]['price'] = f"¥{new_price}"
                            sleep(1)
                            self.listings[r]['status'] = f"✓ -{amount}{inc_sign}"
                        elif self.listings[r]['action'] == 3:
                            # Increase price
                            self.driver.get(self.listings[r]['url'])
                            price = wfe_by_xpath(self.driver, '//mer-price[@data-testid="price"]').get_attribute('value')
                            sleep(1)
                            new_price = get_changed_price(price, by_percent=self.is_percent, unit_amount=self.value, percent_amount=self.percentage, decrease=False)
                            change_price(self.driver, new_price)
                            self.listings[r]['price'] = f"¥{new_price}"
                            self.listings[r]['status'] = f"✓ +{amount}{inc_sign}"
                        elif self.listings[r]['action'] == 4:
                            # Private
                            unpublish_the_published(self.driver, self.listings[r]['url'])
                            self.listings[r]['status'] = "✓ Listings → Unpublished"
                            self.listings[r]['source'] = 'unpublished'
                    elif self.listings[r]['source'] == 'unpublished':
                        publish_the_unpublished(self.driver, self.listings[r]['url'])
                        self.listings[r]['status'] = "✓ Unpublished → Published"
                        self.listings[r]['source'] = 'listings'
                    elif self.listings[r]['source'] == 'drafts':
                        new_url = publish_the_draft(self.driver, self.listings[r]['url'])
                        self.listings[r]['status'] = "✓ Drafts → Published"
                        self.listings[r]['source'] = 'listings'
                        self.listings[r]['url'] = new_url
                    if self.marked_items > product_counter + 1:
                        sleep(self.interval[product_counter])
                except Exception as e:
                    print(e)
                    self.listings[r]['status'] = False
                self.listings[r]['marked'] = False
                product_counter += 1
                self.progress.emit((product_counter+1, self.listings[r]['status']))
            elif self.listings[r]['marked'] and self.listings[r]['action'] != 0 and self.listings[r]['url'] is None:
                self.listings[r]['status'] = False
                self.listings[r]['marked'] = False
                product_counter += 1
                self.progress.emit((product_counter+1, self.listings[r]['status']))
            # updated_listings.append(listing)
        self.decrease_complete.emit(self.listings)
        self.finished.emit()


class UpdateDialog(QDialog):
    def closeEvent(self, event):
        super().closeEvent(event)


class GetListings(QThread):
    complete_signal = Signal(list)
    finished = Signal()
    login_signal = Signal()
    
    def __init__(self, driver):
        super(GetListings, self).__init__()
        self.driver = driver

    def run(self):
        all_listings, successful1 = get_all_listings(self.driver)
        if successful1:
            # self.complete_signal.emit(all_listings)
            all_drafts, successful2 = get_all_drafts(self.driver)
            if successful2:
                # Add 2 lists
                if len(all_listings) == 0 or len(all_drafts) == 0:
                    resultant_list = all_listings + all_drafts
                else:
                    blank_list = [{
                        'url': '',
                        'img': '',
                        'title': '',
                        'price': '',
                        'marked': None,
                        'status': '',
                        'action': None,
                        'source': None
                    }]
                    resultant_list = all_listings + blank_list + all_drafts
                self.complete_signal.emit(resultant_list)
        else:
            self.login_signal.emit()
        self.finished.emit()


class OpenChrome(QThread):
    browser_signal = Signal(webdriver.chrome.webdriver.WebDriver)

    def run(self):
        driver = open_chromedriver(webdriver)
        driver.get('https://jp.mercari.com')
        self.browser_signal.emit(driver)


if __name__ == '__main__':
    application_path = None
    platform_name = platform.system()
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(os.path.abspath(sys.executable))
    elif __file__:
        application_path = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
