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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_PumpingData(object):
    def setupUi(self, PumpingData):
        if not PumpingData.objectName():
            PumpingData.setObjectName(u"PumpingData")
        PumpingData.resize(813, 736)
        self.verticalLayout_2 = QVBoxLayout(PumpingData)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gb_dicharge = QGroupBox(PumpingData)
        self.gb_dicharge.setObjectName(u"gb_dicharge")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_dicharge.sizePolicy().hasHeightForWidth())
        self.gb_dicharge.setSizePolicy(sizePolicy)
        self.gb_dicharge.setMinimumSize(QSize(320, 0))
        self.gb_dicharge.setMaximumSize(QSize(320, 100))
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


        self.verticalLayout_2.addWidget(self.gb_dicharge)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_drawdown = QTableWidget(PumpingData)
        self.table_drawdown.setObjectName(u"table_drawdown")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_drawdown.sizePolicy().hasHeightForWidth())
        self.table_drawdown.setSizePolicy(sizePolicy1)
        self.table_drawdown.setMinimumSize(QSize(320, 0))
        self.table_drawdown.setMaximumSize(QSize(320, 16777215))

        self.verticalLayout.addWidget(self.table_drawdown)

        self.btn_plt_data = QPushButton(PumpingData)
        self.btn_plt_data.setObjectName(u"btn_plt_data")
        sizePolicy.setHeightForWidth(self.btn_plt_data.sizePolicy().hasHeightForWidth())
        self.btn_plt_data.setSizePolicy(sizePolicy)
        self.btn_plt_data.setMinimumSize(QSize(320, 0))
        self.btn_plt_data.setMaximumSize(QSize(320, 16777215))

        self.verticalLayout.addWidget(self.btn_plt_data)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.lbl_scatter_graph_space_hoder = QLabel(PumpingData)
        self.lbl_scatter_graph_space_hoder.setObjectName(u"lbl_scatter_graph_space_hoder")

        self.horizontalLayout.addWidget(self.lbl_scatter_graph_space_hoder)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

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
        self.btn_plt_data.setText(QCoreApplication.translate("PumpingData", u"Plot Data", None))
        self.lbl_scatter_graph_space_hoder.setText(QCoreApplication.translate("PumpingData", u"Space holder", None))
    # retranslateUi

