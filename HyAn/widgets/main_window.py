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


