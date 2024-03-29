import os
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

        # Create a FigureCanvas object and set the size of the figure
        self.view = FigureCanvas(Figure(figsize=(100, 100)))
        self.axes = self.view.figure.subplots()  # Create axes for the plot

        # Set the axes labels and title
        self.axes.set_xlabel("Time [min]")
        self.axes.set_ylabel("Drawdown [m]")
        self.axes.set_title("Analysis Curve")

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.view)

        self.setLayout(vlayout)

    def thies_analysis(self, data):
        """
        Generates a plot of the Theis model fit.

        Args:
        - time: Drawdown time
        - drawdown: Change in water level after pumping started
        - Q: float, pumping rate (in meters^3/day)
        - T: float, Transmissivity
        - S: float, Storativity

        Notes:
        - float value of transmissivity and storativity.
        - Generates a plot of the Theis model fit and saves it as 'analysis.png'.
        - The Theis curved is plotted using the Theis class in the theis.py module.
        """
        obs_data = np.array(data[0][0])

        self.time = obs_data[:, 0]
        self.drawdown = obs_data[:, 1]
        self.Q = data[0][1]  # m3/d

        self.r = data[1]  # m

        # pass data to Theis class and get the results
        self.thies = Theis(self.time, self.drawdown, self.Q, self.r)
        self.T, self.S, self.model = self.thies.fit()

        # plot the results
        self.axes.clear()
        self.axes.set_xlabel("Time [min]")
        self.axes.set_ylabel("Drawdown [m]")
        self.axes.set_title("Analysis Curve")
        self.axes.plot(self.time, self.model, "r-", label="Theis")
        self.axes.plot(self.time, self.drawdown, "bo", label="Data")
        self.view.draw()

        # save the figure
        output_path = os.path.join("HyAn/img", "analysis.png")
        fig = self.view.figure

        fig.savefig(output_path)
