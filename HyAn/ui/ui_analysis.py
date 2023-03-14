# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from HyAn.widgets.analysis_curve import AnalysisCurve
from HyAn.ui.icon import rc_icon

class Ui_Analysis(object):
    def setupUi(self, Analysis):
        if not Analysis.objectName():
            Analysis.setObjectName(u"Analysis")
        Analysis.resize(750, 772)
        self.horizontalLayout = QHBoxLayout(Analysis)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_analysis = QGroupBox(Analysis)
        self.gb_analysis.setObjectName(u"gb_analysis")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_analysis.sizePolicy().hasHeightForWidth())
        self.gb_analysis.setSizePolicy(sizePolicy)
        self.gb_analysis.setMaximumSize(QSize(320, 120))
        self.gridLayout_3 = QGridLayout(self.gb_analysis)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_analysis_name = QLabel(self.gb_analysis)
        self.lbl_analysis_name.setObjectName(u"lbl_analysis_name")

        self.gridLayout_3.addWidget(self.lbl_analysis_name, 0, 0, 1, 1)

        self.l_edit_analysis_name = QLineEdit(self.gb_analysis)
        self.l_edit_analysis_name.setObjectName(u"l_edit_analysis_name")

        self.gridLayout_3.addWidget(self.l_edit_analysis_name, 0, 1, 1, 1)

        self.lbl_analysis_performed_by = QLabel(self.gb_analysis)
        self.lbl_analysis_performed_by.setObjectName(u"lbl_analysis_performed_by")

        self.gridLayout_3.addWidget(self.lbl_analysis_performed_by, 1, 0, 1, 1)

        self.l_edit_analysis_performed_by = QLineEdit(self.gb_analysis)
        self.l_edit_analysis_performed_by.setObjectName(u"l_edit_analysis_performed_by")

        self.gridLayout_3.addWidget(self.l_edit_analysis_performed_by, 1, 1, 1, 1)

        self.lbl_analysis_data = QLabel(self.gb_analysis)
        self.lbl_analysis_data.setObjectName(u"lbl_analysis_data")

        self.gridLayout_3.addWidget(self.lbl_analysis_data, 2, 0, 1, 1)

        self.date_analysis = QDateEdit(self.gb_analysis)
        self.date_analysis.setObjectName(u"date_analysis")

        self.gridLayout_3.addWidget(self.date_analysis, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.gb_analysis)

        self.gb_solution = QGroupBox(Analysis)
        self.gb_solution.setObjectName(u"gb_solution")
        sizePolicy.setHeightForWidth(self.gb_solution.sizePolicy().hasHeightForWidth())
        self.gb_solution.setSizePolicy(sizePolicy)
        self.gb_solution.setMinimumSize(QSize(320, 0))
        self.gb_solution.setMaximumSize(QSize(16777215, 160))
        self.verticalLayout_3 = QVBoxLayout(self.gb_solution)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_fit = QPushButton(self.gb_solution)
        self.btn_fit.setObjectName(u"btn_fit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_fit.sizePolicy().hasHeightForWidth())
        self.btn_fit.setSizePolicy(sizePolicy1)
        self.btn_fit.setMinimumSize(QSize(160, 28))
        self.btn_fit.setMaximumSize(QSize(280, 40))
        icon = QIcon()
        icon.addFile(u":/menu_bar_icon/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fit.setIcon(icon)

        self.verticalLayout_3.addWidget(self.btn_fit)


        self.verticalLayout.addWidget(self.gb_solution)

        self.gb_output = QGroupBox(Analysis)
        self.gb_output.setObjectName(u"gb_output")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gb_output.sizePolicy().hasHeightForWidth())
        self.gb_output.setSizePolicy(sizePolicy2)
        self.gb_output.setMinimumSize(QSize(320, 0))
        self.gb_output.setMaximumSize(QSize(280, 120))
        self.gridLayout_2 = QGridLayout(self.gb_output)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.l_edit_output_transmissivity = QLineEdit(self.gb_output)
        self.l_edit_output_transmissivity.setObjectName(u"l_edit_output_transmissivity")

        self.gridLayout_2.addWidget(self.l_edit_output_transmissivity, 0, 1, 1, 1)

        self.lbl_output_storativity = QLabel(self.gb_output)
        self.lbl_output_storativity.setObjectName(u"lbl_output_storativity")

        self.gridLayout_2.addWidget(self.lbl_output_storativity, 1, 0, 1, 1)

        self.l_edit_output_storativity = QLineEdit(self.gb_output)
        self.l_edit_output_storativity.setObjectName(u"l_edit_output_storativity")

        self.gridLayout_2.addWidget(self.l_edit_output_storativity, 1, 1, 1, 1)

        self.lbl_output_transmissivity = QLabel(self.gb_output)
        self.lbl_output_transmissivity.setObjectName(u"lbl_output_transmissivity")

        self.gridLayout_2.addWidget(self.lbl_output_transmissivity, 0, 0, 1, 1)

        self.btn_generate_report = QPushButton(self.gb_output)
        self.btn_generate_report.setObjectName(u"btn_generate_report")
        self.btn_generate_report.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/menu_bar_icon/report.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_generate_report.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_generate_report, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.gb_output)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.wid_analysis_graph = AnalysisCurve(Analysis)
        self.wid_analysis_graph.setObjectName(u"wid_analysis_graph")

        self.horizontalLayout.addWidget(self.wid_analysis_graph)

#if QT_CONFIG(shortcut)
        self.lbl_analysis_name.setBuddy(self.l_edit_analysis_name)
        self.lbl_analysis_performed_by.setBuddy(self.l_edit_analysis_performed_by)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Analysis)

        QMetaObject.connectSlotsByName(Analysis)
    # setupUi

    def retranslateUi(self, Analysis):
        Analysis.setWindowTitle(QCoreApplication.translate("Analysis", u"Form", None))
        self.gb_analysis.setTitle(QCoreApplication.translate("Analysis", u"Analysis", None))
        self.lbl_analysis_name.setText(QCoreApplication.translate("Analysis", u"Analysis Name:", None))
        self.lbl_analysis_performed_by.setText(QCoreApplication.translate("Analysis", u"Analysis Performed by:", None))
        self.lbl_analysis_data.setText(QCoreApplication.translate("Analysis", u"Analysis date:", None))
        self.gb_solution.setTitle(QCoreApplication.translate("Analysis", u"Solution", None))
        self.btn_fit.setText(QCoreApplication.translate("Analysis", u"Fit Data", None))
        self.gb_output.setTitle(QCoreApplication.translate("Analysis", u"Output", None))
        self.lbl_output_storativity.setText(QCoreApplication.translate("Analysis", u"Storativity:", None))
        self.lbl_output_transmissivity.setText(QCoreApplication.translate("Analysis", u"Transmissivity:", None))
        self.btn_generate_report.setText(QCoreApplication.translate("Analysis", u"Generate Report", None))
    # retranslateUi

