from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from HyAn.ui.ui_pumping_data import Ui_PumpingData
from PySide6.QtCore import Signal
import numpy as np


class PumpingData(QWidget, Ui_PumpingData):
    data_changed = Signal(list)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.labels = ['Time [min]', 'Drawdown [m]']

        self.table_drawdown.setRowCount(20)
        self.table_drawdown.setColumnCount(2)
        self.table_drawdown.setHorizontalHeaderLabels(self.labels)

        self.btn_plt_data.clicked.connect(self.get_data)


    def get_data(self):
        self.data = []
        for row in range(self.table_drawdown.rowCount()):
            row_data = []
            for col in range(self.table_drawdown.columnCount()):
                item = self.table_drawdown.item(row, col)
                if item is not None:
                    row_data.append(float(item.text()))
                else:
                    row_data.append(0.0)
            self.data.append(row_data)
        # self.data = [[3, 0.3], [5, 0.7], [8, 1.3], [12, 2.1], [20, 3.2], [24, 3.6], [30, 4.1],
        #              [38, 4.7], [47, 5.1], [50, 5.3], [60, 5.7], [70, 6.1], [80, 6.3], [90, 6.7],
        #              [100, 7.0], [130, 7.5], [160, 8.3], [200, 8.5], [260, 9.2], [320, 9.7], [380, 10.2], [500, 10.9]]



        self.wid_plt_graph.plot_data(self.data)
        print("get data : ",self.data)
        self.data_changed.emit(self.data)
        return self.data
