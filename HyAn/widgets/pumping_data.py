from PySide6.QtWidgets import QWidget

from HyAn.ui.ui_pumping_data import Ui_PumpingData

class PumpingData(QWidget, Ui_PumpingData):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
