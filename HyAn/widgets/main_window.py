#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow


from HyAn.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.menubar.hide()
        self.toolBar.hide()
        self.showFullScreen()

        self.wid_pumping_data.data_changed.connect(self.wid_analysis.fit_data)

        # self.wid_pumping_test.pumping_test_data_changed.connect(self.get_pumping_test_data)

        self.wid_pumping_test.pumping_test_data_r_changed.connect(
            self.wid_analysis.set_r
        )

        self.wid_analysis.btn_fit.clicked.connect(self.generate_report)

    # def get_pumping_test_data(self, data):

    #     self.pumping_test_data = data

    def generate_report(self):
        self.pumping_data = self.wid_pumping_data.get_report()
        self.pumping_test = self.wid_pumping_test.get_report()

        print(f"Pumping_data : {self.pumping_data}")
        print(f"pumping_test : {self.pumping_test}")
