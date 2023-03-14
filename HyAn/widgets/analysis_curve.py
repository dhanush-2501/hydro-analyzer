import matplotlib

matplotlib.use("Qt5Agg")
from PySide6.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from HyAn.solution.theis import Theis
import numpy as np


class AnalysisCurve(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.T, self.S = 0, 0

        self.view = FigureCanvas(Figure(figsize=(100, 100)))
        self.axes = self.view.figure.subplots()
        self.axes.set_xlabel("Time [min]")
        self.axes.set_ylabel("Drawdown [m]")
        self.axes.set_title("Analysis Curve")
        fig = self.view.figure
        fig.savefig("analysis.png")

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.view)

        self.setLayout(vlayout)

    def thies_analysis(self, data):
        # self.time = data[:, 0]
        # self.drawdown = data[:, 1]
        obs_data = np.array(data[0][0])
        print(f"data : {data}")

        self.time = obs_data[:, 0]
        self.drawdown = obs_data[:, 1]
        self.Q = data[0][1]  # m3/d
        print("q : ", self.Q)

        self.r = data[1]  # m
        print("r : ", self.r)

        self.thies = Theis(self.time, self.drawdown, self.Q, self.r)
        self.T, self.S, self.model = self.thies.fit()
        print(f"t : {self.T}")
        print(f"S : {self.S}")
        print(f"model : {self.model}")

        self.axes.clear()
        self.axes.set_xlabel("Time [min]")
        self.axes.set_ylabel("Drawdown [m]")
        self.axes.set_title("Analysis Curve")
        self.axes.plot(self.time, self.model, "r-", label="Theis")
        self.axes.plot(self.time, self.drawdown, "bo", label="Data")
        self.view.draw()
        fig = self.view.figure
        fig.savefig("analysis.png")
