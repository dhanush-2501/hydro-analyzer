from PySide6.QtWidgets import QWidget

from HyAn.ui.ui_analysis import Ui_Analysis
from PySide6.QtCore import Slot


class Analysis(QWidget, Ui_Analysis):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btn_fit.clicked.connect(self.fit_theis)
        self.S = 0
        self.T = 0

    # gets data from pumping test
    @Slot(list)
    def fit_data(self, data):
        self.theis_data = data
        self.btn_fit.setEnabled(True)

    # gets r from pumping test
    @Slot(float)
    def set_r(self, data):
        self.r = data

    # fits theis data to graph and outputs S and T
    def fit_theis(self):
        self.wid_analysis_graph.thies_analysis([self.theis_data, self.r])
        self.S = round(self.wid_analysis_graph.S, 4)
        self.T = round(self.wid_analysis_graph.T, 4)
        self.l_edit_output_storativity.setText(str(self.S))
        self.l_edit_output_transmissivity.setText(str(self.T))

    def get_s_t(self):
        return {
            "S": self.S,
            "T": self.T,
        }
