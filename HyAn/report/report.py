from fpdf import FPDF
import pandas as pd
from PySide6.QtWidgets import QFileDialog, QWidget
import os


class PDF(FPDF):
    def __init__(self):
        super().__init__()

    def header(self):
        # Page border
        self.rect(5.0, 5.0, self.w - 10.0, self.h - 10.0)

        # File Header
        self.set_font("Arial", "B", 12)
        self.cell(0, 20, "Hydro Analyzer Report", 1, 1, "C")


class Report:
    """
    Generates report for the pumping test analysis.
    """

    def __init__(self, data):
        self.pdf = PDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", "", 12)

        self.m = 10
        self.pw = 210 - 2 * self.m
        self.ch = 10
        self.cw = self.pw / 6

        self.data = data
        print("Time in report", list(data[:, 0]))

        # time and drawdown data frame
        self.df = pd.DataFrame({"Time": list(data[:, 0]), "Drawdown": list(data[:, 1])})

    def project_data(
        self,
        project_name,
        project_number,
        client,
        location,
        pumping_test,
        pumping_well,
        test_conducted_by,
        test_date,
        discharge_rate,
    ):
        # datas of the project and analyst
        self.pdf.cell(
            w=(self.pw / 3), h=self.ch, txt=f"Project : {project_name} ", border=1, ln=0
        )
        self.pdf.cell(
            w=(self.pw / 3),
            h=self.ch,
            txt=f"Project Number : {project_number} ",
            border=1,
            ln=0,
        )
        self.pdf.cell(
            w=(self.pw / 3), h=self.ch, txt=f"Client : {client} ", border=1, ln=1
        )

        self.pdf.cell(
            w=(self.pw / 3), h=self.ch, txt=f"Location : {location}", border=1, ln=0
        )
        self.pdf.cell(
            w=(self.pw / 3),
            h=self.ch,
            txt=f"Pumping Test: {pumping_test}",
            border=1,
            ln=0,
        )
        self.pdf.cell(
            w=(self.pw / 3),
            h=self.ch,
            txt=f"Pumping well: {pumping_well}",
            border=1,
            ln=1,
        )

        self.pdf.cell(
            w=(self.pw / 3),
            h=self.ch,
            txt=f"Test Conducted By : {test_conducted_by}",
            border=1,
            ln=0,
        )
        self.pdf.cell(
            w=(self.pw / 3), h=self.ch, txt=f"Test Date : {test_date}", border=1, ln=0
        )
        self.pdf.cell(
            w=(self.pw / 3),
            h=self.ch,
            txt=f"Discharge rate : {discharge_rate} ",
            border=1,
            ln=1,
        )

    def print_table(self):
        # Table Header
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(w=self.cw, h=10, txt="Time", border=1, ln=0, align="C")
        self.pdf.cell(w=self.cw, h=10, txt="Drawdown", border=1, ln=1, align="C")

        # Table Data
        self.pdf.set_font("Arial", "", 14)
        for i in range(0, len(self.df)):
            self.pdf.cell(
                w=self.cw,
                h=6,
                txt=self.df["Time"].iloc[i].astype(str),
                border=1,
                ln=0,
                align="C",
            )
            self.pdf.cell(
                w=self.cw,
                h=6,
                txt=self.df["Drawdown"].iloc[i].astype(str),
                border=1,
                ln=1,
                align="C",
            )

    def display_graph(self):
        # embedding graph on report
        output_path = os.path.join("HyAn/img", "analysis.png")
        self.pdf.image(output_path, x=72, y=65, w=130, h=125, type="PNG")

    def result(self, t, s):
        # Transmissivity and storativity Cell
        self.pdf.ln(10)
        self.pdf.cell(
            w=self.pw, h=self.ch, txt=f"Transmissivity : {t} ", border=1, ln=1
        )
        self.pdf.cell(w=self.pw, h=self.ch, txt=f"Storativity : {s}", border=1, ln=1)

    def generate_report(self, output_path):
        # generates report pdf
        self.pdf.output(f"{output_path}", "F")
