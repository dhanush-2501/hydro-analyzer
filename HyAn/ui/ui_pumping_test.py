# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pumping_test.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QTimeEdit, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_table_well_information(object):
    def setupUi(self, table_well_information):
        if not table_well_information.objectName():
            table_well_information.setObjectName(u"table_well_information")
        table_well_information.resize(1277, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(table_well_information.sizePolicy().hasHeightForWidth())
        table_well_information.setSizePolicy(sizePolicy)
        table_well_information.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(table_well_information)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gb_project_informataion = QGroupBox(table_well_information)
        self.gb_project_informataion.setObjectName(u"gb_project_informataion")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gb_project_informataion.sizePolicy().hasHeightForWidth())
        self.gb_project_informataion.setSizePolicy(sizePolicy1)
        self.gb_project_informataion.setMinimumSize(QSize(0, 0))
        self.gb_project_informataion.setMaximumSize(QSize(320, 16777215))
        self.formLayout_2 = QFormLayout(self.gb_project_informataion)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_project_name = QLabel(self.gb_project_informataion)
        self.lbl_project_name.setObjectName(u"lbl_project_name")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_project_name)

        self.l_edit_project_name = QLineEdit(self.gb_project_informataion)
        self.l_edit_project_name.setObjectName(u"l_edit_project_name")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.l_edit_project_name)

        self.lbl_project_number = QLabel(self.gb_project_informataion)
        self.lbl_project_number.setObjectName(u"lbl_project_number")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_project_number)

        self.l_edit_project_number = QLineEdit(self.gb_project_informataion)
        self.l_edit_project_number.setObjectName(u"l_edit_project_number")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.l_edit_project_number)

        self.lbl_client = QLabel(self.gb_project_informataion)
        self.lbl_client.setObjectName(u"lbl_client")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_client)

        self.l_edit__client = QLineEdit(self.gb_project_informataion)
        self.l_edit__client.setObjectName(u"l_edit__client")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.l_edit__client)

        self.lbl_location = QLabel(self.gb_project_informataion)
        self.lbl_location.setObjectName(u"lbl_location")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_location)

        self.l_edit_location = QLineEdit(self.gb_project_informataion)
        self.l_edit_location.setObjectName(u"l_edit_location")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.l_edit_location)


        self.horizontalLayout.addWidget(self.gb_project_informataion)

        self.gb_units = QGroupBox(table_well_information)
        self.gb_units.setObjectName(u"gb_units")
        self.gb_units.setMinimumSize(QSize(400, 0))
        self.gb_units.setMaximumSize(QSize(320, 16777215))
        self.gridLayout_2 = QGridLayout(self.gb_units)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_site_plan_2 = QLabel(self.gb_units)
        self.lbl_site_plan_2.setObjectName(u"lbl_site_plan_2")

        self.gridLayout_2.addWidget(self.lbl_site_plan_2, 0, 0, 1, 1)

        self.cb_site_plan_2 = QComboBox(self.gb_units)
        self.cb_site_plan_2.addItem("")
        self.cb_site_plan_2.addItem("")
        self.cb_site_plan_2.addItem("")
        self.cb_site_plan_2.addItem("")
        self.cb_site_plan_2.addItem("")
        self.cb_site_plan_2.setObjectName(u"cb_site_plan_2")

        self.gridLayout_2.addWidget(self.cb_site_plan_2, 0, 1, 1, 1)

        self.lbl_dimensions_2 = QLabel(self.gb_units)
        self.lbl_dimensions_2.setObjectName(u"lbl_dimensions_2")

        self.gridLayout_2.addWidget(self.lbl_dimensions_2, 0, 2, 1, 1)

        self.cb_dimensions_2 = QComboBox(self.gb_units)
        self.cb_dimensions_2.addItem("")
        self.cb_dimensions_2.addItem("")
        self.cb_dimensions_2.addItem("")
        self.cb_dimensions_2.addItem("")
        self.cb_dimensions_2.addItem("")
        self.cb_dimensions_2.setObjectName(u"cb_dimensions_2")

        self.gridLayout_2.addWidget(self.cb_dimensions_2, 0, 3, 1, 1)

        self.lbl_time_2 = QLabel(self.gb_units)
        self.lbl_time_2.setObjectName(u"lbl_time_2")

        self.gridLayout_2.addWidget(self.lbl_time_2, 1, 0, 1, 1)

        self.cb_time_2 = QComboBox(self.gb_units)
        self.cb_time_2.addItem("")
        self.cb_time_2.addItem("")
        self.cb_time_2.addItem("")
        self.cb_time_2.addItem("")
        self.cb_time_2.setObjectName(u"cb_time_2")

        self.gridLayout_2.addWidget(self.cb_time_2, 1, 1, 1, 1)

        self.lbl_discharge_2 = QLabel(self.gb_units)
        self.lbl_discharge_2.setObjectName(u"lbl_discharge_2")

        self.gridLayout_2.addWidget(self.lbl_discharge_2, 1, 2, 1, 1)

        self.cb_discharge_2 = QComboBox(self.gb_units)
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.addItem("")
        self.cb_discharge_2.setObjectName(u"cb_discharge_2")

        self.gridLayout_2.addWidget(self.cb_discharge_2, 1, 3, 1, 1)

        self.lbl_transmissivity_2 = QLabel(self.gb_units)
        self.lbl_transmissivity_2.setObjectName(u"lbl_transmissivity_2")

        self.gridLayout_2.addWidget(self.lbl_transmissivity_2, 2, 0, 1, 1)

        self.cb_transmissivity_2 = QComboBox(self.gb_units)
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.addItem("")
        self.cb_transmissivity_2.setObjectName(u"cb_transmissivity_2")

        self.gridLayout_2.addWidget(self.cb_transmissivity_2, 2, 1, 1, 1)

        self.lbl_pressure_2 = QLabel(self.gb_units)
        self.lbl_pressure_2.setObjectName(u"lbl_pressure_2")

        self.gridLayout_2.addWidget(self.lbl_pressure_2, 2, 2, 1, 1)

        self.cb_pressure_2 = QComboBox(self.gb_units)
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.setObjectName(u"cb_pressure_2")

        self.gridLayout_2.addWidget(self.cb_pressure_2, 2, 3, 1, 1)


        self.horizontalLayout.addWidget(self.gb_units)

        self.gb_pumping_test = QGroupBox(table_well_information)
        self.gb_pumping_test.setObjectName(u"gb_pumping_test")
        self.gb_pumping_test.setMaximumSize(QSize(320, 16777215))
        self.formLayout_10 = QFormLayout(self.gb_pumping_test)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.lbl_pumping_test_name = QLabel(self.gb_pumping_test)
        self.lbl_pumping_test_name.setObjectName(u"lbl_pumping_test_name")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.lbl_pumping_test_name)

        self.l_edit_pumping_test_name = QLineEdit(self.gb_pumping_test)
        self.l_edit_pumping_test_name.setObjectName(u"l_edit_pumping_test_name")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.l_edit_pumping_test_name)

        self.lbl_pumping_test_performed_by = QLabel(self.gb_pumping_test)
        self.lbl_pumping_test_performed_by.setObjectName(u"lbl_pumping_test_performed_by")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.lbl_pumping_test_performed_by)

        self.l_edit_pumping_test_performed_by = QLineEdit(self.gb_pumping_test)
        self.l_edit_pumping_test_performed_by.setObjectName(u"l_edit_pumping_test_performed_by")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.l_edit_pumping_test_performed_by)

        self.lbl_pumping_test_date_time = QLabel(self.gb_pumping_test)
        self.lbl_pumping_test_date_time.setObjectName(u"lbl_pumping_test_date_time")

        self.formLayout_10.setWidget(4, QFormLayout.LabelRole, self.lbl_pumping_test_date_time)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.time_puming_test = QTimeEdit(self.gb_pumping_test)
        self.time_puming_test.setObjectName(u"time_puming_test")

        self.horizontalLayout_2.addWidget(self.time_puming_test)

        self.date_pumping_test = QDateEdit(self.gb_pumping_test)
        self.date_pumping_test.setObjectName(u"date_pumping_test")

        self.horizontalLayout_2.addWidget(self.date_pumping_test)


        self.formLayout_10.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.gb_pumping_test)

        self.gb_aquifer_properties = QGroupBox(table_well_information)
        self.gb_aquifer_properties.setObjectName(u"gb_aquifer_properties")
        self.gb_aquifer_properties.setMaximumSize(QSize(280, 16777215))
        self.formLayout_11 = QFormLayout(self.gb_aquifer_properties)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.lbl_aquifer_thickness = QLabel(self.gb_aquifer_properties)
        self.lbl_aquifer_thickness.setObjectName(u"lbl_aquifer_thickness")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.lbl_aquifer_thickness)

        self.l_edit_aquifer_thickness = QLineEdit(self.gb_aquifer_properties)
        self.l_edit_aquifer_thickness.setObjectName(u"l_edit_aquifer_thickness")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.l_edit_aquifer_thickness)

        self.lbl_aquifer_type = QLabel(self.gb_aquifer_properties)
        self.lbl_aquifer_type.setObjectName(u"lbl_aquifer_type")
        self.lbl_aquifer_type.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.lbl_aquifer_type)

        self.cb_aquifer_type = QComboBox(self.gb_aquifer_properties)
        self.cb_aquifer_type.addItem("")
        self.cb_aquifer_type.addItem("")
        self.cb_aquifer_type.addItem("")
        self.cb_aquifer_type.addItem("")
        self.cb_aquifer_type.addItem("")
        self.cb_aquifer_type.setObjectName(u"cb_aquifer_type")

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.cb_aquifer_type)


        self.horizontalLayout.addWidget(self.gb_aquifer_properties)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.hl_pumping_test_aquifer_properties = QHBoxLayout()
        self.hl_pumping_test_aquifer_properties.setObjectName(u"hl_pumping_test_aquifer_properties")

        self.verticalLayout.addLayout(self.hl_pumping_test_aquifer_properties)

        self.vl_tabe_image = QVBoxLayout()
        self.vl_tabe_image.setObjectName(u"vl_tabe_image")
        self.table_well_data = QTableView(table_well_information)
        self.table_well_data.setObjectName(u"table_well_data")

        self.vl_tabe_image.addWidget(self.table_well_data)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_create_new_well = QPushButton(table_well_information)
        self.btn_create_new_well.setObjectName(u"btn_create_new_well")
        self.btn_create_new_well.setMinimumSize(QSize(400, 0))
        self.btn_create_new_well.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_create_new_well)

        self.btn_submit = QPushButton(table_well_information)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(400, 0))
        self.btn_submit.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_submit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.vl_tabe_image.addLayout(self.horizontalLayout_3)

        self.lbl_image = QLabel(table_well_information)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setPixmap(QPixmap(u":/menu_bar_icon/well_demo.png"))

        self.vl_tabe_image.addWidget(self.lbl_image)


        self.verticalLayout.addLayout(self.vl_tabe_image)

#if QT_CONFIG(shortcut)
        self.lbl_project_name.setBuddy(self.l_edit_project_name)
        self.lbl_project_number.setBuddy(self.l_edit_project_number)
        self.lbl_client.setBuddy(self.l_edit__client)
        self.lbl_location.setBuddy(self.l_edit_location)
        self.lbl_pumping_test_name.setBuddy(self.l_edit_pumping_test_name)
        self.lbl_pumping_test_performed_by.setBuddy(self.l_edit_pumping_test_performed_by)
        self.lbl_aquifer_thickness.setBuddy(self.l_edit_aquifer_thickness)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(table_well_information)

        QMetaObject.connectSlotsByName(table_well_information)
    # setupUi

    def retranslateUi(self, table_well_information):
        table_well_information.setWindowTitle(QCoreApplication.translate("table_well_information", u"Form", None))
        self.gb_project_informataion.setTitle(QCoreApplication.translate("table_well_information", u"Project Information", None))
        self.lbl_project_name.setText(QCoreApplication.translate("table_well_information", u"Project Name:", None))
        self.lbl_project_number.setText(QCoreApplication.translate("table_well_information", u"Project Number:", None))
        self.lbl_client.setText(QCoreApplication.translate("table_well_information", u"Client:", None))
        self.lbl_location.setText(QCoreApplication.translate("table_well_information", u"Location:", None))
        self.gb_units.setTitle(QCoreApplication.translate("table_well_information", u"Units", None))
        self.lbl_site_plan_2.setText(QCoreApplication.translate("table_well_information", u"Site Plan:", None))
        self.cb_site_plan_2.setItemText(0, QCoreApplication.translate("table_well_information", u"mm", None))
        self.cb_site_plan_2.setItemText(1, QCoreApplication.translate("table_well_information", u"cm", None))
        self.cb_site_plan_2.setItemText(2, QCoreApplication.translate("table_well_information", u"m", None))
        self.cb_site_plan_2.setItemText(3, QCoreApplication.translate("table_well_information", u"ft", None))
        self.cb_site_plan_2.setItemText(4, QCoreApplication.translate("table_well_information", u"in", None))

        self.lbl_dimensions_2.setText(QCoreApplication.translate("table_well_information", u"Dimensions:", None))
        self.cb_dimensions_2.setItemText(0, QCoreApplication.translate("table_well_information", u"m", None))
        self.cb_dimensions_2.setItemText(1, QCoreApplication.translate("table_well_information", u"cm", None))
        self.cb_dimensions_2.setItemText(2, QCoreApplication.translate("table_well_information", u"mm", None))
        self.cb_dimensions_2.setItemText(3, QCoreApplication.translate("table_well_information", u"ft", None))
        self.cb_dimensions_2.setItemText(4, QCoreApplication.translate("table_well_information", u"in", None))

        self.lbl_time_2.setText(QCoreApplication.translate("table_well_information", u"Time:", None))
        self.cb_time_2.setItemText(0, QCoreApplication.translate("table_well_information", u"sec", None))
        self.cb_time_2.setItemText(1, QCoreApplication.translate("table_well_information", u"min", None))
        self.cb_time_2.setItemText(2, QCoreApplication.translate("table_well_information", u"hr", None))
        self.cb_time_2.setItemText(3, QCoreApplication.translate("table_well_information", u"day", None))

        self.lbl_discharge_2.setText(QCoreApplication.translate("table_well_information", u"Discharge:", None))
        self.cb_discharge_2.setItemText(0, QCoreApplication.translate("table_well_information", u"m\u00b3/sec", None))
        self.cb_discharge_2.setItemText(1, QCoreApplication.translate("table_well_information", u"m\u00b3/min", None))
        self.cb_discharge_2.setItemText(2, QCoreApplication.translate("table_well_information", u"m\u00b3/hr", None))
        self.cb_discharge_2.setItemText(3, QCoreApplication.translate("table_well_information", u"m\u00b3/day", None))
        self.cb_discharge_2.setItemText(4, QCoreApplication.translate("table_well_information", u"l/s", None))
        self.cb_discharge_2.setItemText(5, QCoreApplication.translate("table_well_information", u"ft\u00b3/sec", None))
        self.cb_discharge_2.setItemText(6, QCoreApplication.translate("table_well_information", u"ft\u00b3/min", None))
        self.cb_discharge_2.setItemText(7, QCoreApplication.translate("table_well_information", u"ft\u00b3/hr", None))
        self.cb_discharge_2.setItemText(8, QCoreApplication.translate("table_well_information", u"ft\u00b3/day", None))
        self.cb_discharge_2.setItemText(9, QCoreApplication.translate("table_well_information", u"U.S gal/min", None))
        self.cb_discharge_2.setItemText(10, QCoreApplication.translate("table_well_information", u"U.S gal/day", None))
        self.cb_discharge_2.setItemText(11, QCoreApplication.translate("table_well_information", u"U.K gal/min", None))
        self.cb_discharge_2.setItemText(12, QCoreApplication.translate("table_well_information", u"U.K gal/day", None))

        self.lbl_transmissivity_2.setText(QCoreApplication.translate("table_well_information", u"Transmissivity:", None))
        self.cb_transmissivity_2.setItemText(0, QCoreApplication.translate("table_well_information", u"m\u00b2/sec", None))
        self.cb_transmissivity_2.setItemText(1, QCoreApplication.translate("table_well_information", u"m\u00b2/min", None))
        self.cb_transmissivity_2.setItemText(2, QCoreApplication.translate("table_well_information", u"m\u00b2/hr", None))
        self.cb_transmissivity_2.setItemText(3, QCoreApplication.translate("table_well_information", u"m\u00b2/day", None))
        self.cb_transmissivity_2.setItemText(4, QCoreApplication.translate("table_well_information", u"ft\u00b2/sec", None))
        self.cb_transmissivity_2.setItemText(5, QCoreApplication.translate("table_well_information", u"ft\u00b2/min", None))
        self.cb_transmissivity_2.setItemText(6, QCoreApplication.translate("table_well_information", u"ft\u00b2/hr", None))
        self.cb_transmissivity_2.setItemText(7, QCoreApplication.translate("table_well_information", u"ft\u00b2/day", None))
        self.cb_transmissivity_2.setItemText(8, QCoreApplication.translate("table_well_information", u"gal/day-ft", None))
        self.cb_transmissivity_2.setItemText(9, QCoreApplication.translate("table_well_information", u"cm\u00b2/sec", None))

        self.lbl_pressure_2.setText(QCoreApplication.translate("table_well_information", u"Pressure:", None))
        self.cb_pressure_2.setItemText(0, QCoreApplication.translate("table_well_information", u"Pa", None))
        self.cb_pressure_2.setItemText(1, QCoreApplication.translate("table_well_information", u"bar", None))
        self.cb_pressure_2.setItemText(2, QCoreApplication.translate("table_well_information", u"mbar", None))
        self.cb_pressure_2.setItemText(3, QCoreApplication.translate("table_well_information", u"mm Hg", None))
        self.cb_pressure_2.setItemText(4, QCoreApplication.translate("table_well_information", u"atm", None))
        self.cb_pressure_2.setItemText(5, QCoreApplication.translate("table_well_information", u"at", None))
        self.cb_pressure_2.setItemText(6, QCoreApplication.translate("table_well_information", u"psi", None))

        self.gb_pumping_test.setTitle(QCoreApplication.translate("table_well_information", u"Pumping Test", None))
        self.lbl_pumping_test_name.setText(QCoreApplication.translate("table_well_information", u"Name:", None))
        self.lbl_pumping_test_performed_by.setText(QCoreApplication.translate("table_well_information", u"Performed by:", None))
        self.lbl_pumping_test_date_time.setText(QCoreApplication.translate("table_well_information", u"Date/Time:", None))
        self.gb_aquifer_properties.setTitle(QCoreApplication.translate("table_well_information", u"Aquifer Properties", None))
        self.lbl_aquifer_thickness.setText(QCoreApplication.translate("table_well_information", u"Thickness[m]:", None))
        self.lbl_aquifer_type.setText(QCoreApplication.translate("table_well_information", u"Type:", None))
        self.cb_aquifer_type.setItemText(0, QCoreApplication.translate("table_well_information", u"Unknown", None))
        self.cb_aquifer_type.setItemText(1, QCoreApplication.translate("table_well_information", u"Confined", None))
        self.cb_aquifer_type.setItemText(2, QCoreApplication.translate("table_well_information", u"Unconfined", None))
        self.cb_aquifer_type.setItemText(3, QCoreApplication.translate("table_well_information", u"Leaky", None))
        self.cb_aquifer_type.setItemText(4, QCoreApplication.translate("table_well_information", u"Fracture", None))

        self.btn_create_new_well.setText(QCoreApplication.translate("table_well_information", u"Create a New Well", None))
        self.btn_submit.setText(QCoreApplication.translate("table_well_information", u"Submit", None))
        self.lbl_image.setText("")
    # retranslateUi

