import sys
from PySide6.QtWidgets import QApplication
from HyAn.widgets.main_window import MainWindow


# main function
def main():
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
