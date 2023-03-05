from PySide6.QtWidgets import QWidget

from HyAn.ui.ui_pumping_test import Ui_PumpingTest

class PumpingTest(QWidget, Ui_PumpingTest):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
