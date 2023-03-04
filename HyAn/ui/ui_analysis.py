# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_analysis.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 772)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_analysis = QGroupBox(Form)
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

        self.gb_solution = QGroupBox(Form)
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

        self.cb_apply_graph_setting = QComboBox(self.gb_solution)
        self.cb_apply_graph_setting.addItem("")
        self.cb_apply_graph_setting.addItem("")
        self.cb_apply_graph_setting.setObjectName(u"cb_apply_graph_setting")
        sizePolicy1.setHeightForWidth(self.cb_apply_graph_setting.sizePolicy().hasHeightForWidth())
        self.cb_apply_graph_setting.setSizePolicy(sizePolicy1)
        self.cb_apply_graph_setting.setMinimumSize(QSize(0, 28))
        self.cb_apply_graph_setting.setMaximumSize(QSize(280, 40))

        self.verticalLayout_3.addWidget(self.cb_apply_graph_setting)

        self.cb_analysis_method = QComboBox(self.gb_solution)
        self.cb_analysis_method.addItem("")
        self.cb_analysis_method.addItem("")
        self.cb_analysis_method.addItem("")
        self.cb_analysis_method.addItem("")
        self.cb_analysis_method.addItem("")
        self.cb_analysis_method.setObjectName(u"cb_analysis_method")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_analysis_method.sizePolicy().hasHeightForWidth())
        self.cb_analysis_method.setSizePolicy(sizePolicy2)
        self.cb_analysis_method.setMinimumSize(QSize(0, 28))
        self.cb_analysis_method.setMaximumSize(QSize(280, 40))

        self.verticalLayout_3.addWidget(self.cb_analysis_method)


        self.verticalLayout.addWidget(self.gb_solution)

        self.gb_output = QGroupBox(Form)
        self.gb_output.setObjectName(u"gb_output")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gb_output.sizePolicy().hasHeightForWidth())
        self.gb_output.setSizePolicy(sizePolicy3)
        self.gb_output.setMinimumSize(QSize(320, 0))
        self.gb_output.setMaximumSize(QSize(280, 120))
        self.gridLayout_2 = QGridLayout(self.gb_output)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_output_transmissivity = QLabel(self.gb_output)
        self.lbl_output_transmissivity.setObjectName(u"lbl_output_transmissivity")

        self.gridLayout_2.addWidget(self.lbl_output_transmissivity, 0, 0, 1, 1)

        self.lbl_output_storativity = QLabel(self.gb_output)
        self.lbl_output_storativity.setObjectName(u"lbl_output_storativity")

        self.gridLayout_2.addWidget(self.lbl_output_storativity, 1, 0, 1, 1)

        self.l_edit_output_transmissivity = QLineEdit(self.gb_output)
        self.l_edit_output_transmissivity.setObjectName(u"l_edit_output_transmissivity")

        self.gridLayout_2.addWidget(self.l_edit_output_transmissivity, 0, 1, 1, 1)

        self.btn_generate_report = QPushButton(self.gb_output)
        self.btn_generate_report.setObjectName(u"btn_generate_report")
        icon1 = QIcon()
        icon1.addFile(u":/menu_bar_icon/report.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_generate_report.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_generate_report, 2, 0, 1, 2)

        self.l_edit_output_storativity = QLineEdit(self.gb_output)
        self.l_edit_output_storativity.setObjectName(u"l_edit_output_storativity")

        self.gridLayout_2.addWidget(self.l_edit_output_storativity, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.gb_output)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.lbl_output_graph = QLabel(Form)
        self.lbl_output_graph.setObjectName(u"lbl_output_graph")

        self.horizontalLayout.addWidget(self.lbl_output_graph)

#if QT_CONFIG(shortcut)
        self.lbl_analysis_name.setBuddy(self.l_edit_analysis_name)
        self.lbl_analysis_performed_by.setBuddy(self.l_edit_analysis_performed_by)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gb_analysis.setTitle(QCoreApplication.translate("Form", u"Analysis", None))
        self.lbl_analysis_name.setText(QCoreApplication.translate("Form", u"Analysis Name:", None))
        self.lbl_analysis_performed_by.setText(QCoreApplication.translate("Form", u"Analysis Performed by:", None))
        self.lbl_analysis_data.setText(QCoreApplication.translate("Form", u"Analysis date:", None))
        self.gb_solution.setTitle(QCoreApplication.translate("Form", u"Solution", None))
        self.btn_fit.setText(QCoreApplication.translate("Form", u"Fit", None))
        self.cb_apply_graph_setting.setItemText(0, QCoreApplication.translate("Form", u"Apply Graph Setting", None))
        self.cb_apply_graph_setting.setItemText(1, QCoreApplication.translate("Form", u"log - log", None))

        self.cb_analysis_method.setItemText(0, QCoreApplication.translate("Form", u"Analysis Method", None))
        self.cb_analysis_method.setItemText(1, QCoreApplication.translate("Form", u"Theis (Confined)", None))
        self.cb_analysis_method.setItemText(2, QCoreApplication.translate("Form", u"Cooper Jacob (Confined)", None))
        self.cb_analysis_method.setItemText(3, QCoreApplication.translate("Form", u"Theis  (Unconfined)", None))
        self.cb_analysis_method.setItemText(4, QCoreApplication.translate("Form", u"Cooper Jacob  (Unconfined)", None))

        self.gb_output.setTitle(QCoreApplication.translate("Form", u"Output", None))
        self.lbl_output_transmissivity.setText(QCoreApplication.translate("Form", u"Transmissivity:", None))
        self.lbl_output_storativity.setText(QCoreApplication.translate("Form", u"Storativity:", None))
        self.btn_generate_report.setText(QCoreApplication.translate("Form", u"Generate Report", None))
        self.lbl_output_graph.setText(QCoreApplication.translate("Form", u"Graph", None))
    # retranslateUi

