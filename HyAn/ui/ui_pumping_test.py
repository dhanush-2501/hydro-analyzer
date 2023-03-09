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
    QSpacerItem, QTableWidget, QTableWidgetItem, QTimeEdit,
    QVBoxLayout, QWidget)
import HyAn.ui.icon.rc_icon

class Ui_PumpingTest(object):
    def setupUi(self, PumpingTest):
        if not PumpingTest.objectName():
            PumpingTest.setObjectName(u"PumpingTest")
        PumpingTest.resize(1032, 796)
        self.verticalLayout = QVBoxLayout(PumpingTest)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hl_project_info_units = QHBoxLayout()
        self.hl_project_info_units.setObjectName(u"hl_project_info_units")
        self.gb_project_informataion = QGroupBox(PumpingTest)
        self.gb_project_informataion.setObjectName(u"gb_project_informataion")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_project_informataion.sizePolicy().hasHeightForWidth())
        self.gb_project_informataion.setSizePolicy(sizePolicy)
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


        self.hl_project_info_units.addWidget(self.gb_project_informataion)

        self.gb_units = QGroupBox(PumpingTest)
        self.gb_units.setObjectName(u"gb_units")
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
        self.cb_pressure_2.addItem("")
        self.cb_pressure_2.setObjectName(u"cb_pressure_2")

        self.gridLayout_2.addWidget(self.cb_pressure_2, 2, 3, 1, 1)


        self.hl_project_info_units.addWidget(self.gb_units)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_project_info_units.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.hl_project_info_units)

        self.hl_pumping_test_aquifer_properties = QHBoxLayout()
        self.hl_pumping_test_aquifer_properties.setObjectName(u"hl_pumping_test_aquifer_properties")
        self.gb_pumping_test = QGroupBox(PumpingTest)
        self.gb_pumping_test.setObjectName(u"gb_pumping_test")
        self.gb_pumping_test.setMaximumSize(QSize(320, 16777215))
        self.formLayout_10 = QFormLayout(self.gb_pumping_test)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.lbl_pumping_test_name = QLabel(self.gb_pumping_test)
        self.lbl_pumping_test_name.setObjectName(u"lbl_pumping_test_name")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.lbl_pumping_test_name)

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

        self.lbl_pumping_test_performed_by = QLabel(self.gb_pumping_test)
        self.lbl_pumping_test_performed_by.setObjectName(u"lbl_pumping_test_performed_by")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.lbl_pumping_test_performed_by)

        self.l_edit_pumping_test_performed_by = QLineEdit(self.gb_pumping_test)
        self.l_edit_pumping_test_performed_by.setObjectName(u"l_edit_pumping_test_performed_by")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.l_edit_pumping_test_performed_by)

        self.l_edit_pumping_test_name = QLineEdit(self.gb_pumping_test)
        self.l_edit_pumping_test_name.setObjectName(u"l_edit_pumping_test_name")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.l_edit_pumping_test_name)


        self.hl_pumping_test_aquifer_properties.addWidget(self.gb_pumping_test)

        self.gb_aquifer_properties = QGroupBox(PumpingTest)
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
        self.cb_aquifer_type.addItem("")
        self.cb_aquifer_type.setObjectName(u"cb_aquifer_type")

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.cb_aquifer_type)


        self.hl_pumping_test_aquifer_properties.addWidget(self.gb_aquifer_properties)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_pumping_test_aquifer_properties.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.hl_pumping_test_aquifer_properties)

        self.vl_tabe_image = QVBoxLayout()
        self.vl_tabe_image.setObjectName(u"vl_tabe_image")
        self.table_well_information = QTableWidget(PumpingTest)
        if (self.table_well_information.columnCount() < 15):
            self.table_well_information.setColumnCount(15)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_well_information.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        if (self.table_well_information.rowCount() < 3):
            self.table_well_information.setRowCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_well_information.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_well_information.setVerticalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_well_information.setVerticalHeaderItem(2, __qtablewidgetitem17)
        self.table_well_information.setObjectName(u"table_well_information")

        self.vl_tabe_image.addWidget(self.table_well_information)

        self.btn_create_new_well = QPushButton(PumpingTest)
        self.btn_create_new_well.setObjectName(u"btn_create_new_well")

        self.vl_tabe_image.addWidget(self.btn_create_new_well)

        self.lbl_image = QLabel(PumpingTest)
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

        self.retranslateUi(PumpingTest)

        QMetaObject.connectSlotsByName(PumpingTest)
    # setupUi

    def retranslateUi(self, PumpingTest):
        PumpingTest.setWindowTitle(QCoreApplication.translate("PumpingTest", u"Form", None))
        self.gb_project_informataion.setTitle(QCoreApplication.translate("PumpingTest", u"Project Information", None))
        self.lbl_project_name.setText(QCoreApplication.translate("PumpingTest", u"Project Name:", None))
        self.lbl_project_number.setText(QCoreApplication.translate("PumpingTest", u"Project Number:", None))
        self.lbl_client.setText(QCoreApplication.translate("PumpingTest", u"Client:", None))
        self.lbl_location.setText(QCoreApplication.translate("PumpingTest", u"Location:", None))
        self.gb_units.setTitle(QCoreApplication.translate("PumpingTest", u"Units", None))
        self.lbl_site_plan_2.setText(QCoreApplication.translate("PumpingTest", u"Site Plan:", None))
        self.cb_site_plan_2.setItemText(0, "")
        self.cb_site_plan_2.setItemText(1, QCoreApplication.translate("PumpingTest", u"mm", None))
        self.cb_site_plan_2.setItemText(2, QCoreApplication.translate("PumpingTest", u"cm", None))
        self.cb_site_plan_2.setItemText(3, QCoreApplication.translate("PumpingTest", u"m", None))
        self.cb_site_plan_2.setItemText(4, QCoreApplication.translate("PumpingTest", u"ft", None))
        self.cb_site_plan_2.setItemText(5, QCoreApplication.translate("PumpingTest", u"in", None))

        self.lbl_dimensions_2.setText(QCoreApplication.translate("PumpingTest", u"Dimensions:", None))
        self.cb_dimensions_2.setItemText(0, "")
        self.cb_dimensions_2.setItemText(1, QCoreApplication.translate("PumpingTest", u"m", None))
        self.cb_dimensions_2.setItemText(2, QCoreApplication.translate("PumpingTest", u"cm", None))
        self.cb_dimensions_2.setItemText(3, QCoreApplication.translate("PumpingTest", u"mm", None))
        self.cb_dimensions_2.setItemText(4, QCoreApplication.translate("PumpingTest", u"ft", None))
        self.cb_dimensions_2.setItemText(5, QCoreApplication.translate("PumpingTest", u"in", None))

        self.lbl_time_2.setText(QCoreApplication.translate("PumpingTest", u"Time:", None))
        self.cb_time_2.setItemText(0, "")
        self.cb_time_2.setItemText(1, QCoreApplication.translate("PumpingTest", u"sec", None))
        self.cb_time_2.setItemText(2, QCoreApplication.translate("PumpingTest", u"min", None))
        self.cb_time_2.setItemText(3, QCoreApplication.translate("PumpingTest", u"hr", None))
        self.cb_time_2.setItemText(4, QCoreApplication.translate("PumpingTest", u"day", None))

        self.lbl_discharge_2.setText(QCoreApplication.translate("PumpingTest", u"Discharge:", None))
        self.cb_discharge_2.setItemText(0, "")
        self.cb_discharge_2.setItemText(1, QCoreApplication.translate("PumpingTest", u"m\u00b3/sec", None))
        self.cb_discharge_2.setItemText(2, QCoreApplication.translate("PumpingTest", u"m\u00b3/min", None))
        self.cb_discharge_2.setItemText(3, QCoreApplication.translate("PumpingTest", u"m\u00b3/hr", None))
        self.cb_discharge_2.setItemText(4, QCoreApplication.translate("PumpingTest", u"m\u00b3/day", None))
        self.cb_discharge_2.setItemText(5, QCoreApplication.translate("PumpingTest", u"l/s", None))
        self.cb_discharge_2.setItemText(6, QCoreApplication.translate("PumpingTest", u"ft\u00b3/sec", None))
        self.cb_discharge_2.setItemText(7, QCoreApplication.translate("PumpingTest", u"ft\u00b3/min", None))
        self.cb_discharge_2.setItemText(8, QCoreApplication.translate("PumpingTest", u"ft\u00b3/hr", None))
        self.cb_discharge_2.setItemText(9, QCoreApplication.translate("PumpingTest", u"ft\u00b3/day", None))
        self.cb_discharge_2.setItemText(10, QCoreApplication.translate("PumpingTest", u"U.S gal/min", None))
        self.cb_discharge_2.setItemText(11, QCoreApplication.translate("PumpingTest", u"U.S gal/day", None))
        self.cb_discharge_2.setItemText(12, QCoreApplication.translate("PumpingTest", u"U.K gal/min", None))
        self.cb_discharge_2.setItemText(13, QCoreApplication.translate("PumpingTest", u"U.K gal/day", None))

        self.lbl_transmissivity_2.setText(QCoreApplication.translate("PumpingTest", u"Transmissivity:", None))
        self.cb_transmissivity_2.setItemText(0, "")
        self.cb_transmissivity_2.setItemText(1, QCoreApplication.translate("PumpingTest", u"m\u00b2/sec", None))
        self.cb_transmissivity_2.setItemText(2, QCoreApplication.translate("PumpingTest", u"m\u00b2/min", None))
        self.cb_transmissivity_2.setItemText(3, QCoreApplication.translate("PumpingTest", u"m\u00b2/hr", None))
        self.cb_transmissivity_2.setItemText(4, QCoreApplication.translate("PumpingTest", u"m\u00b2/day", None))
        self.cb_transmissivity_2.setItemText(5, QCoreApplication.translate("PumpingTest", u"ft\u00b2/sec", None))
        self.cb_transmissivity_2.setItemText(6, QCoreApplication.translate("PumpingTest", u"ft\u00b2/min", None))
        self.cb_transmissivity_2.setItemText(7, QCoreApplication.translate("PumpingTest", u"ft\u00b2/hr", None))
        self.cb_transmissivity_2.setItemText(8, QCoreApplication.translate("PumpingTest", u"ft\u00b2/day", None))
        self.cb_transmissivity_2.setItemText(9, QCoreApplication.translate("PumpingTest", u"gal/day-ft", None))
        self.cb_transmissivity_2.setItemText(10, QCoreApplication.translate("PumpingTest", u"cm\u00b2/sec", None))

        self.lbl_pressure_2.setText(QCoreApplication.translate("PumpingTest", u"Pressure:", None))
        self.cb_pressure_2.setItemText(0, "")
        self.cb_pressure_2.setItemText(1, QCoreApplication.translate("PumpingTest", u"Pa", None))
        self.cb_pressure_2.setItemText(2, QCoreApplication.translate("PumpingTest", u"bar", None))
        self.cb_pressure_2.setItemText(3, QCoreApplication.translate("PumpingTest", u"mbar", None))
        self.cb_pressure_2.setItemText(4, QCoreApplication.translate("PumpingTest", u"mm Hg", None))
        self.cb_pressure_2.setItemText(5, QCoreApplication.translate("PumpingTest", u"atm", None))
        self.cb_pressure_2.setItemText(6, QCoreApplication.translate("PumpingTest", u"at", None))
        self.cb_pressure_2.setItemText(7, QCoreApplication.translate("PumpingTest", u"psi", None))

        self.gb_pumping_test.setTitle(QCoreApplication.translate("PumpingTest", u"Pumping Test", None))
        self.lbl_pumping_test_name.setText(QCoreApplication.translate("PumpingTest", u"Name:", None))
        self.lbl_pumping_test_date_time.setText(QCoreApplication.translate("PumpingTest", u"Date/Time:", None))
        self.lbl_pumping_test_performed_by.setText(QCoreApplication.translate("PumpingTest", u"Performed by:", None))
        self.gb_aquifer_properties.setTitle(QCoreApplication.translate("PumpingTest", u"Aquifer Properties", None))
        self.lbl_aquifer_thickness.setText(QCoreApplication.translate("PumpingTest", u"Thickness[m]:", None))
        self.lbl_aquifer_type.setText(QCoreApplication.translate("PumpingTest", u"Type:", None))
        self.cb_aquifer_type.setItemText(0, "")
        self.cb_aquifer_type.setItemText(1, QCoreApplication.translate("PumpingTest", u"Unknown", None))
        self.cb_aquifer_type.setItemText(2, QCoreApplication.translate("PumpingTest", u"Confined", None))
        self.cb_aquifer_type.setItemText(3, QCoreApplication.translate("PumpingTest", u"Unconfined", None))
        self.cb_aquifer_type.setItemText(4, QCoreApplication.translate("PumpingTest", u"Leaky", None))
        self.cb_aquifer_type.setItemText(5, QCoreApplication.translate("PumpingTest", u"Fracture", None))

        ___qtablewidgetitem = self.table_well_information.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PumpingTest", u"S.No", None));
        ___qtablewidgetitem1 = self.table_well_information.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PumpingTest", u"Name", None));
        ___qtablewidgetitem2 = self.table_well_information.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PumpingTest", u"Type", None));
        ___qtablewidgetitem3 = self.table_well_information.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PumpingTest", u"X[m]", None));
        ___qtablewidgetitem4 = self.table_well_information.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PumpingTest", u"Y[m]", None));
        ___qtablewidgetitem5 = self.table_well_information.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PumpingTest", u"Elevation", None));
        ___qtablewidgetitem6 = self.table_well_information.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PumpingTest", u"Benchmark", None));
        ___qtablewidgetitem7 = self.table_well_information.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PumpingTest", u"Penetration", None));
        ___qtablewidgetitem8 = self.table_well_information.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PumpingTest", u"R[m]", None));
        ___qtablewidgetitem9 = self.table_well_information.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PumpingTest", u"L[m]", None));
        ___qtablewidgetitem10 = self.table_well_information.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PumpingTest", u"b[m]", None));
        ___qtablewidgetitem11 = self.table_well_information.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PumpingTest", u"r[m]", None));
        ___qtablewidgetitem12 = self.table_well_information.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PumpingTest", u"B[m]", None));
        ___qtablewidgetitem13 = self.table_well_information.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PumpingTest", u"n[%]", None));
        ___qtablewidgetitem14 = self.table_well_information.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PumpingTest", u"use r[w]", None));
        self.btn_create_new_well.setText(QCoreApplication.translate("PumpingTest", u"Create a New Well", None))
        self.lbl_image.setText("")
    # retranslateUi

