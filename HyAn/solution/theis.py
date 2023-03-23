import numpy as np
import math
from scipy.optimize import curve_fit


class Theis:
    def __init__(self, time, drawdown, Q, r):
        self.T = 0.0
        self.S = 0.0
        self.r = r
        self.Q = Q
        self.time = time
        self.drawdown = drawdown
        self.initial_guess = [1, 0.00001]
        self.bounds = ([0.01, 0.000001], [100000, 0.1])
        self.model = []

    def calculate_well_function(self, r, S, T, t):
        """
        Calculates the well function used in the Theis equation.

        Args:
        - r: float, distance from the pumping well to the observation well (in meters)
        - S: float, specific storage (in meters^-1)
        - T: float, transmissivity (in meters^2/day)
        - t: float or numpy array, time(s) since pumping started (in days)

        Returns:
        - float or numpy array, value(s) of the well function at the specified time(s)
        """
        
        u = (r**2) * S / (4 * T * t)
        Wu = -0.5772 - np.log(u) + u
        n_terms = 30
        for i in range(2, n_terms + 1):
            sign = (-1) ** (i - 1)
            factorial = np.math.factorial(i)
            Wu += sign * (u**i) / (i * factorial)
        print(f"calculate well func : {[r, S, T, t]}")
        print(f"wu : {Wu}")
        return Wu

    def calculate_drawdown(self, t, T, S):
        """
        Calculates the drawdown at different times using the Theis equation.

        Args:
        - T: float, transmissivity (in meters^2/day)
        - S: float, specific storage (in meters^-1)
        - Q: float, pumping rate (in cubic meters/day)
        - r: float, distance from the pumping well to the observation well (in meters)
        - t: numpy array, time(s) since pumping started (in days)

        Returns:
        - numpy array, drawdown(s) at the specified time(s)
        """
        pi = math.pi
        n = len(t)
        drawdown = np.zeros(n)
        for i in range(n):
            Wu_val = self.calculate_well_function(self.r, S, T, t[i])
            drawdown[i] = self.Q * Wu_val / (4 * pi * T)
        print(f"drawdown : {drawdown}")
        return drawdown

    def fit(self):
        popt, pcov = curve_fit(
            self.calculate_drawdown,
            self.time,
            self.drawdown,
            p0=self.initial_guess,
            bounds=self.bounds,
        )
        self.T = popt[0]
        self.S = popt[1]
        self.model = list(self.calculate_drawdown(self.time, self.T, self.S))
        print(f"fit : {[self.T, self.S, self.model]}")
        return [self.T, self.S, self.model]

time = [3, 5, 8, 12, 20, 24, 30, 38, 47, 50, 60, 70, 80, 90, 100, 130, 160, 200, 260, 320, 380, 500]
drawdown = [0.3, 0.7, 1.3, 2.1, 3.2, 3.6, 4.1, 4.7, 5.1, 5.3, 5.7, 6.1, 6.3, 6.7, 7.0, 7.5, 8.3, 8.5, 9.2, 9.7, 10.2, 10.9]
Q = 220
r = 40

theis = Theis(time=time, drawdown=drawdown, Q=Q, r=r)
theis.fit()