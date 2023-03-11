from PySide6.QtWidgets import QWidget

from HyAn.ui.ui_pumping_data import Ui_PumpingData

class PumpingData(QWidget, Ui_PumpingData):
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
                    row_data.append(item.text())
                else:
                    row_data.append('')
            self.data.append(row_data)
        print(self.data)
        self.wid_plt_graph.plot_data(self.data)
        
        
