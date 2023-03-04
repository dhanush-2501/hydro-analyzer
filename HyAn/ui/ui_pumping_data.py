# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pumping_data.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PumpingData(object):
    def setupUi(self, PumpingData):
        if not PumpingData.objectName():
            PumpingData.setObjectName(u"PumpingData")
        PumpingData.resize(813, 736)
        self.verticalLayout = QVBoxLayout(PumpingData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_dicharge = QGroupBox(PumpingData)
        self.gb_dicharge.setObjectName(u"gb_dicharge")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_dicharge.sizePolicy().hasHeightForWidth())
        self.gb_dicharge.setSizePolicy(sizePolicy)
        self.gb_dicharge.setMaximumSize(QSize(16777215, 100))
        self.formLayout_4 = QFormLayout(self.gb_dicharge)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lbl_constant = QLabel(self.gb_dicharge)
        self.lbl_constant.setObjectName(u"lbl_constant")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lbl_constant)

        self.l_edit_constant = QLineEdit(self.gb_dicharge)
        self.l_edit_constant.setObjectName(u"l_edit_constant")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.l_edit_constant)

        self.l_edit_static_wl = QLineEdit(self.gb_dicharge)
        self.l_edit_static_wl.setObjectName(u"l_edit_static_wl")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.l_edit_static_wl)

        self.lbl_static_wl = QLabel(self.gb_dicharge)
        self.lbl_static_wl.setObjectName(u"lbl_static_wl")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.lbl_static_wl)


        self.verticalLayout.addWidget(self.gb_dicharge)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_dicharge_time = QTableWidget(PumpingData)
        if (self.table_dicharge_time.columnCount() < 2):
            self.table_dicharge_time.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_dicharge_time.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_dicharge_time.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table_dicharge_time.rowCount() < 21):
            self.table_dicharge_time.setRowCount(21)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(15, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(16, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(17, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(18, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(19, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_dicharge_time.setVerticalHeaderItem(20, __qtablewidgetitem22)
        self.table_dicharge_time.setObjectName(u"table_dicharge_time")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_dicharge_time.sizePolicy().hasHeightForWidth())
        self.table_dicharge_time.setSizePolicy(sizePolicy1)
        self.table_dicharge_time.setMinimumSize(QSize(280, 0))

        self.horizontalLayout.addWidget(self.table_dicharge_time)

        self.table_drawdown = QTableWidget(PumpingData)
        if (self.table_drawdown.columnCount() < 3):
            self.table_drawdown.setColumnCount(3)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_drawdown.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_drawdown.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_drawdown.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        if (self.table_drawdown.rowCount() < 21):
            self.table_drawdown.setRowCount(21)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(10, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(11, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(12, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(13, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(14, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(15, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(16, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(17, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(18, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(19, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_drawdown.setVerticalHeaderItem(20, __qtablewidgetitem46)
        self.table_drawdown.setObjectName(u"table_drawdown")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_drawdown.sizePolicy().hasHeightForWidth())
        self.table_drawdown.setSizePolicy(sizePolicy2)
        self.table_drawdown.setMinimumSize(QSize(280, 0))

        self.horizontalLayout.addWidget(self.table_drawdown)

        self.lbl_scatter_graph_space_hoder = QLabel(PumpingData)
        self.lbl_scatter_graph_space_hoder.setObjectName(u"lbl_scatter_graph_space_hoder")

        self.horizontalLayout.addWidget(self.lbl_scatter_graph_space_hoder)


        self.verticalLayout.addLayout(self.horizontalLayout)

#if QT_CONFIG(shortcut)
        self.lbl_constant.setBuddy(self.l_edit_constant)
        self.lbl_static_wl.setBuddy(self.l_edit_static_wl)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(PumpingData)

        QMetaObject.connectSlotsByName(PumpingData)
    # setupUi

    def retranslateUi(self, PumpingData):
        PumpingData.setWindowTitle(QCoreApplication.translate("PumpingData", u"Form", None))
        self.gb_dicharge.setTitle(QCoreApplication.translate("PumpingData", u"Discharge[m\u00b3/sec]", None))
        self.lbl_constant.setText(QCoreApplication.translate("PumpingData", u"Constant:", None))
        self.lbl_static_wl.setText(QCoreApplication.translate("PumpingData", u"Static WL [m]:", None))
        ___qtablewidgetitem = self.table_dicharge_time.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PumpingData", u"Time[s]", None));
        ___qtablewidgetitem1 = self.table_dicharge_time.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PumpingData", u"Discharge[m\u00b3/s]", None));
        ___qtablewidgetitem2 = self.table_dicharge_time.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PumpingData", u"1", None));
        ___qtablewidgetitem3 = self.table_dicharge_time.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PumpingData", u"2", None));
        ___qtablewidgetitem4 = self.table_dicharge_time.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PumpingData", u"3", None));
        ___qtablewidgetitem5 = self.table_dicharge_time.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PumpingData", u"4", None));
        ___qtablewidgetitem6 = self.table_dicharge_time.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PumpingData", u"5", None));
        ___qtablewidgetitem7 = self.table_dicharge_time.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PumpingData", u"6", None));
        ___qtablewidgetitem8 = self.table_dicharge_time.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PumpingData", u"7", None));
        ___qtablewidgetitem9 = self.table_dicharge_time.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PumpingData", u"8", None));
        ___qtablewidgetitem10 = self.table_dicharge_time.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PumpingData", u"9", None));
        ___qtablewidgetitem11 = self.table_dicharge_time.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PumpingData", u"10", None));
        ___qtablewidgetitem12 = self.table_dicharge_time.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PumpingData", u"11", None));
        ___qtablewidgetitem13 = self.table_dicharge_time.verticalHeaderItem(12)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PumpingData", u"12", None));
        ___qtablewidgetitem14 = self.table_dicharge_time.verticalHeaderItem(13)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PumpingData", u"13", None));
        ___qtablewidgetitem15 = self.table_dicharge_time.verticalHeaderItem(14)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("PumpingData", u"14", None));
        ___qtablewidgetitem16 = self.table_dicharge_time.verticalHeaderItem(15)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("PumpingData", u"15", None));
        ___qtablewidgetitem17 = self.table_dicharge_time.verticalHeaderItem(16)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("PumpingData", u"16", None));
        ___qtablewidgetitem18 = self.table_dicharge_time.verticalHeaderItem(17)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("PumpingData", u"17", None));
        ___qtablewidgetitem19 = self.table_dicharge_time.verticalHeaderItem(18)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("PumpingData", u"18", None));
        ___qtablewidgetitem20 = self.table_dicharge_time.verticalHeaderItem(19)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("PumpingData", u"19", None));
        ___qtablewidgetitem21 = self.table_dicharge_time.verticalHeaderItem(20)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("PumpingData", u"20", None));
        ___qtablewidgetitem22 = self.table_drawdown.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("PumpingData", u"Time [s]", None));
        ___qtablewidgetitem23 = self.table_drawdown.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("PumpingData", u"Water Level [m]", None));
        ___qtablewidgetitem24 = self.table_drawdown.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("PumpingData", u"Drawdown [m]", None));
        ___qtablewidgetitem25 = self.table_drawdown.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("PumpingData", u"1", None));
        ___qtablewidgetitem26 = self.table_drawdown.verticalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("PumpingData", u"2", None));
        ___qtablewidgetitem27 = self.table_drawdown.verticalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("PumpingData", u"3", None));
        ___qtablewidgetitem28 = self.table_drawdown.verticalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("PumpingData", u"4", None));
        ___qtablewidgetitem29 = self.table_drawdown.verticalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("PumpingData", u"5", None));
        ___qtablewidgetitem30 = self.table_drawdown.verticalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("PumpingData", u"6", None));
        ___qtablewidgetitem31 = self.table_drawdown.verticalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("PumpingData", u"7", None));
        ___qtablewidgetitem32 = self.table_drawdown.verticalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("PumpingData", u"8", None));
        ___qtablewidgetitem33 = self.table_drawdown.verticalHeaderItem(9)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("PumpingData", u"9", None));
        ___qtablewidgetitem34 = self.table_drawdown.verticalHeaderItem(10)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("PumpingData", u"10", None));
        ___qtablewidgetitem35 = self.table_drawdown.verticalHeaderItem(11)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("PumpingData", u"11", None));
        ___qtablewidgetitem36 = self.table_drawdown.verticalHeaderItem(12)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("PumpingData", u"12", None));
        ___qtablewidgetitem37 = self.table_drawdown.verticalHeaderItem(13)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("PumpingData", u"13", None));
        ___qtablewidgetitem38 = self.table_drawdown.verticalHeaderItem(14)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("PumpingData", u"14", None));
        ___qtablewidgetitem39 = self.table_drawdown.verticalHeaderItem(15)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("PumpingData", u"15", None));
        ___qtablewidgetitem40 = self.table_drawdown.verticalHeaderItem(16)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("PumpingData", u"16", None));
        ___qtablewidgetitem41 = self.table_drawdown.verticalHeaderItem(17)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("PumpingData", u"17", None));
        ___qtablewidgetitem42 = self.table_drawdown.verticalHeaderItem(18)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("PumpingData", u"18", None));
        ___qtablewidgetitem43 = self.table_drawdown.verticalHeaderItem(19)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("PumpingData", u"19", None));
        ___qtablewidgetitem44 = self.table_drawdown.verticalHeaderItem(20)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("PumpingData", u"20", None));
        self.lbl_scatter_graph_space_hoder.setText(QCoreApplication.translate("PumpingData", u"Space holder", None))
    # retranslateUi

