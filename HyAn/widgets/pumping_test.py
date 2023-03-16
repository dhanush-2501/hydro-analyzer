from PySide6.QtWidgets import QWidget

from HyAn.ui.ui_pumping_test import Ui_PumpingTest
from PySide6.QtCore import Signal


class PumpingTest(QWidget, Ui_PumpingTest):
    pumping_test_data_changed = Signal(list)
    pumping_test_data_r_changed = Signal(float)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.btn_create_new_well.hide()

        # labels for table
        self.labels = [
            "Name",
            "Type",
            "X[m]",
            "Y[m]",
            "B[m]",
            "L[m]",
            "R[m]",
            "b[m]",
            "r[m]",
        ]

        # set table
        self.table_well_information.setRowCount(1)
        self.table_well_information.setColumnCount(9)
        self.table_well_information.setHorizontalHeaderLabels(self.labels)

        self.btn_create_new_well.clicked.connect(self.create_new_well)
        self.btn_submit.clicked.connect(self.get_data)  # get data from table

        self.data = []

    def create_new_well(self):
        current_row = self.table_well_information.rowCount()
        self.table_well_information.setRowCount(current_row + 1)

    def get_data(self):
        self.data = []
        for row in range(self.table_well_information.rowCount()):
            row_data = []
            for col in range(self.table_well_information.columnCount()):
                item = self.table_well_information.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            self.data.append(row_data)
        self.pumping_test_data_changed.emit(self.data)
        self.pumping_test_data_r_changed.emit(float(self.data[0][-1]))
        print(f"self.data[0][-1] : {self.data[0][-1]}")
        print(self.data)

    def get_report(self):
        self.report = {
            "project_name": self.l_edit_project_name.text(),
            "project_number": self.l_edit_project_number.text(),
            "project_client": self.l_edit__client.text(),
            "project_location": self.l_edit_location.text(),
            "pumping_test_name": self.l_edit_pumping_test_name.text(),
            "performed_by": self.l_edit_pumping_test_performed_by.text(),
            "date": self.date_pumping_test.text(),
            "time": self.time_puming_test.text(),
            "well_info": self.data,
            "aquifer_thickness": self.l_edit_aquifer_thickness.text(),
            "aquifer_type": self.lbl_aquifer_type.text(),
        }

        return self.report
