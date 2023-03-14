import matplotlib

matplotlib.use("Qt5Agg")
from PySide6.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np


class DrawdownCurve(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = FigureCanvas(Figure(figsize=(100, 100)))
        self.axes = self.view.figure.subplots()
        self.axes.set_xlabel("Time [min]")
        self.axes.set_ylabel("Drawdown [m]")
        self.axes.set_title("Drawdown Curve")

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.view)

        self.setLayout(vlayout)

    def plot_data(self, data):
        self.data = np.array(data)
        time = self.data[:, 0]
        drawdown = self.data[:, 1]

    
        self.axes.clear() # Clear the axes  before plotting
        # Set the axes labels and title
        self.axes.set_xlabel("Time [min]")
        self.axes.set_ylabel("Drawdown [m]")
        self.axes.set_title("Drawdown Curve")
        self.axes.plot(time, drawdown, "-o") # plot the data
        self.view.draw() # update the canvas
