#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QFileDialog


from HyAn.ui.ui_main_window import Ui_MainWindow
from HyAn.report.report import Report


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.menubar.hide()
        self.toolBar.hide()
        self.showFullScreen()

        # pass data from pumping data widget to analysis widget
        self.wid_pumping_data.data_changed.connect(self.wid_analysis.fit_data)

        # pass r from pumping test widget to analysis widget
        self.wid_pumping_test.pumping_test_data_r_changed.connect(
            self.wid_analysis.set_r
        )

        # generate report
        self.wid_analysis.btn_generate_report.clicked.connect(self.generate_report)

    def generate_report(self):
        """
        Generates the report for the pumping test.

        Notes:
        -update the parameters "self.pumping data" and "self.pumping test" with the reports obtained from the GUI widgets.
        """
        self.pumping_data = self.wid_pumping_data.get_report()
        self.pumping_test = self.wid_pumping_test.get_report()
        self.analysis_data = self.wid_analysis.get_s_t()


        self.project_name = self.pumping_test["project_name"]
        self.project_number = self.pumping_test["project_number"]
        self.project_client = self.pumping_test["project_client"]

        self.project_location = self.pumping_test["project_location"]
        self.pumping_test_name = self.pumping_test["pumping_test_name"]
        self.pumping_well_name = self.pumping_test["well_info"]
        self.pumping_well_name = self.pumping_well_name[0][0]

        self.performed_by = self.pumping_test["performed_by"]
        self.date = self.pumping_test["date"]
        self.discharge_rate = self.pumping_data["Q"]

        self.S = self.analysis_data["S"]
        self.T = self.analysis_data["T"]

        self.data = self.pumping_data["data"]

        self.options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getSaveFileName(
            self, "save analysis report", "", "PDF Files (*.pdf)", options=self.options
        )

        if not self.file_name.endswith(".pdf"):
            self.file_name += ".pdf"

        self.report = Report(self.data)

        self.report.project_data(
            self.project_name,
            self.project_number,
            self.project_client,
            self.project_location,
            self.pumping_test_name,
            self.pumping_well_name,
            self.performed_by,
            self.date,
            self.discharge_rate,
        )
        self.report.print_table()
        self.report.display_graph()
        self.report.result(self.T, self.S)
        self.report.generate_report(self.file_name)