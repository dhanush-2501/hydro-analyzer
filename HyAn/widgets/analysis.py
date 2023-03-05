from PySide6.QtWidgets import QWidget

from HyAn.ui.ui_analysis import Ui_Analysis

class Analysis(QWidget, Ui_Analysis):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
