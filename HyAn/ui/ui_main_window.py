# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QStatusBar,
    QTabWidget,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from HyAn.widgets.analysis import Analysis
from HyAn.widgets.pumping_data import PumpingData
from HyAn.widgets.pumping_test import PumpingTest
from HyAn.ui.icon import rc_icon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 722)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1400, 0))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.t_actionnew = QAction(MainWindow)
        self.t_actionnew.setObjectName("t_actionnew")
        icon = QIcon()
        icon.addFile(
            ":/menu_bar_icon/create file.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.t_actionnew.setIcon(icon)
        self.t_actionopen = QAction(MainWindow)
        self.t_actionopen.setObjectName("t_actionopen")
        icon1 = QIcon()
        icon1.addFile(
            ":/menu_bar_icon/open-folder.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.t_actionopen.setIcon(icon1)
        self.actionClose_Ctrl_Q_ = QAction(MainWindow)
        self.actionClose_Ctrl_Q_.setObjectName("actionClose_Ctrl_Q_")
        self.t_actionsave = QAction(MainWindow)
        self.t_actionsave.setObjectName("t_actionsave")
        icon2 = QIcon()
        icon2.addFile(":/menu_bar_icon/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.t_actionsave.setIcon(icon2)
        self.m_actionsave_as = QAction(MainWindow)
        self.m_actionsave_as.setObjectName("m_actionsave_as")
        self.t_actionprint = QAction(MainWindow)
        self.t_actionprint.setObjectName("t_actionprint")
        icon3 = QIcon()
        icon3.addFile(":/menu_bar_icon/printer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.t_actionprint.setIcon(icon3)
        self.m_actionexit = QAction(MainWindow)
        self.m_actionexit.setObjectName("m_actionexit")
        icon4 = QIcon()
        icon4.addFile(":/menu_bar_icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actionexit.setIcon(icon4)
        self.t_actioncopy = QAction(MainWindow)
        self.t_actioncopy.setObjectName("t_actioncopy")
        icon5 = QIcon()
        icon5.addFile(":/menu_bar_icon/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.t_actioncopy.setIcon(icon5)
        self.t_actionpaste = QAction(MainWindow)
        self.t_actionpaste.setObjectName("t_actionpaste")
        icon6 = QIcon()
        icon6.addFile(":/menu_bar_icon/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.t_actionpaste.setIcon(icon6)
        self.m_actiondelete = QAction(MainWindow)
        self.m_actiondelete.setObjectName("m_actiondelete")
        icon7 = QIcon()
        icon7.addFile(":/menu_bar_icon/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actiondelete.setIcon(icon7)
        self.m_actionnavigation_panel = QAction(MainWindow)
        self.m_actionnavigation_panel.setObjectName("m_actionnavigation_panel")
        self.m_actionnavigation_panel.setCheckable(True)
        self.m_actionnavigation_panel.setChecked(True)
        self.m_actionanalysis_panel = QAction(MainWindow)
        self.m_actionanalysis_panel.setObjectName("m_actionanalysis_panel")
        self.m_actionanalysis_panel.setCheckable(True)
        self.m_actionanalysis_status = QAction(MainWindow)
        self.m_actionanalysis_status.setObjectName("m_actionanalysis_status")
        self.m_actionanalysis_parameter = QAction(MainWindow)
        self.m_actionanalysis_parameter.setObjectName("m_actionanalysis_parameter")
        icon8 = QIcon()
        icon8.addFile(":/menu_bar_icon/scroll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actionanalysis_parameter.setIcon(icon8)
        self.m_actionScatter_diagram = QAction(MainWindow)
        self.m_actionScatter_diagram.setObjectName("m_actionScatter_diagram")
        icon9 = QIcon()
        icon9.addFile(":/menu_bar_icon/scatter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actionScatter_diagram.setIcon(icon9)
        self.m_actioncreate_a_pumping_test = QAction(MainWindow)
        self.m_actioncreate_a_pumping_test.setObjectName(
            "m_actioncreate_a_pumping_test"
        )
        self.m_actioncreate_a_pumping_test_predicition = QAction(MainWindow)
        self.m_actioncreate_a_pumping_test_predicition.setObjectName(
            "m_actioncreate_a_pumping_test_predicition"
        )
        self.m_actioncreate_new_analysis = QAction(MainWindow)
        self.m_actioncreate_new_analysis.setObjectName("m_actioncreate_new_analysis")
        icon10 = QIcon()
        icon10.addFile(":/menu_bar_icon/insert.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actioncreate_new_analysis.setIcon(icon10)
        self.m_actionfit = QAction(MainWindow)
        self.m_actionfit.setObjectName("m_actionfit")
        icon11 = QIcon()
        icon11.addFile(":/menu_bar_icon/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actionfit.setIcon(icon11)
        self.m_actioncomments = QAction(MainWindow)
        self.m_actioncomments.setObjectName("m_actioncomments")
        icon12 = QIcon()
        icon12.addFile(":/menu_bar_icon/comment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actioncomments.setIcon(icon12)
        self.actionDuplicate = QAction(MainWindow)
        self.actionDuplicate.setObjectName("actionDuplicate")
        self.m_actioncontent = QAction(MainWindow)
        self.m_actioncontent.setObjectName("m_actioncontent")
        icon13 = QIcon()
        icon13.addFile(":/menu_bar_icon/content.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actioncontent.setIcon(icon13)
        self.m_actionweb = QAction(MainWindow)
        self.m_actionweb.setObjectName("m_actionweb")
        self.m_actiontutorial = QAction(MainWindow)
        self.m_actiontutorial.setObjectName("m_actiontutorial")
        self.m_actionabout = QAction(MainWindow)
        self.m_actionabout.setObjectName("m_actionabout")
        icon14 = QIcon()
        icon14.addFile(":/menu_bar_icon/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.m_actionabout.setIcon(icon14)
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionRefresh.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab_hydro = QTabWidget(self.centralwidget)
        self.tab_hydro.setObjectName("tab_hydro")
        self.tab_hydro.setEnabled(True)
        self.tab_hydro.setMinimumSize(QSize(0, 0))
        self.tab_puming_test = QWidget()
        self.tab_puming_test.setObjectName("tab_puming_test")
        self.verticalLayout_10 = QVBoxLayout(self.tab_puming_test)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.wid_pumping_test = PumpingTest(self.tab_puming_test)
        self.wid_pumping_test.setObjectName("wid_pumping_test")
        self.wid_pumping_test.setMinimumSize(QSize(1000, 0))

        self.verticalLayout_10.addWidget(self.wid_pumping_test)

        icon15 = QIcon()
        icon15.addFile(
            ":/menu_bar_icon/pumping_test.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.tab_hydro.addTab(self.tab_puming_test, icon15, "")
        self.tab_pumping_data = QWidget()
        self.tab_pumping_data.setObjectName("tab_pumping_data")
        self.verticalLayout_2 = QVBoxLayout(self.tab_pumping_data)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wid_pumping_data = PumpingData(self.tab_pumping_data)
        self.wid_pumping_data.setObjectName("wid_pumping_data")

        self.verticalLayout_2.addWidget(self.wid_pumping_data)

        icon16 = QIcon()
        icon16.addFile(
            ":/menu_bar_icon/water_wiz.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.tab_hydro.addTab(self.tab_pumping_data, icon16, "")
        self.tab_analysis = QWidget()
        self.tab_analysis.setObjectName("tab_analysis")
        self.horizontalLayout = QHBoxLayout(self.tab_analysis)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wid_analysis = Analysis(self.tab_analysis)
        self.wid_analysis.setObjectName("wid_analysis")

        self.horizontalLayout.addWidget(self.wid_analysis)

        icon17 = QIcon()
        icon17.addFile(":/menu_bar_icon/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_hydro.addTab(self.tab_analysis, icon17, "")

        self.verticalLayout_4.addWidget(self.tab_hydro)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1400, 26))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_test = QMenu(self.menubar)
        self.menu_test.setObjectName("menu_test")
        self.menu_analysis = QMenu(self.menubar)
        self.menu_analysis.setObjectName("menu_analysis")
        self.menu_tools = QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setEnabled(True)
        self.toolBar.setMinimumSize(QSize(1200, 0))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_test.menuAction())
        self.menubar.addAction(self.menu_analysis.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menu_file.addAction(self.t_actionnew)
        self.menu_file.addAction(self.t_actionopen)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.t_actionsave)
        self.menu_file.addAction(self.m_actionsave_as)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.t_actionprint)
        self.menu_file.addAction(self.m_actionexit)
        self.menu_edit.addAction(self.t_actioncopy)
        self.menu_edit.addAction(self.t_actionpaste)
        self.menu_edit.addAction(self.m_actiondelete)
        self.menu_view.addAction(self.m_actionnavigation_panel)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.m_actionanalysis_panel)
        self.menu_view.addAction(self.m_actionanalysis_status)
        self.menu_view.addAction(self.m_actionanalysis_parameter)
        self.menu_view.addAction(self.m_actionScatter_diagram)
        self.menu_test.addAction(self.m_actioncreate_a_pumping_test)
        self.menu_test.addAction(self.m_actioncreate_a_pumping_test_predicition)
        self.menu_analysis.addAction(self.m_actioncreate_new_analysis)
        self.menu_analysis.addSeparator()
        self.menu_analysis.addAction(self.m_actionfit)
        self.menu_analysis.addAction(self.m_actioncomments)
        self.menu_analysis.addSeparator()
        self.menu_tools.addAction(self.m_actioncontent)
        self.menu_tools.addAction(self.m_actionweb)
        self.menu_tools.addAction(self.m_actiontutorial)
        self.menu_tools.addSeparator()
        self.menu_tools.addAction(self.m_actionabout)
        self.toolBar.addAction(self.t_actionnew)
        self.toolBar.addAction(self.t_actionopen)
        self.toolBar.addAction(self.t_actionsave)
        self.toolBar.addAction(self.t_actionprint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.t_actioncopy)
        self.toolBar.addAction(self.t_actionpaste)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tab_hydro.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.t_actionnew.setText(QCoreApplication.translate("MainWindow", "New", None))
        # if QT_CONFIG(tooltip)
        self.t_actionnew.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Create a New File (Ctril+N)", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.t_actionnew.setStatusTip(
            QCoreApplication.translate("MainWindow", "Create a new file", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.t_actionnew.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.t_actionopen.setText(
            QCoreApplication.translate("MainWindow", "Open ", None)
        )
        # if QT_CONFIG(tooltip)
        self.t_actionopen.setToolTip(
            QCoreApplication.translate("MainWindow", "Open a File(Ctrl+O)", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.t_actionopen.setStatusTip(
            QCoreApplication.translate("MainWindow", "Open an existing file", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.t_actionopen.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionClose_Ctrl_Q_.setText(
            QCoreApplication.translate("MainWindow", "Close", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionClose_Ctrl_Q_.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Q", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.t_actionsave.setText(
            QCoreApplication.translate("MainWindow", "Save", None)
        )
        # if QT_CONFIG(tooltip)
        self.t_actionsave.setToolTip(
            QCoreApplication.translate("MainWindow", "Save the File(Ctrl+S)", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.t_actionsave.setStatusTip(
            QCoreApplication.translate("MainWindow", "Save the current file ", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.t_actionsave.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.m_actionsave_as.setText(
            QCoreApplication.translate("MainWindow", "Save As", None)
        )
        # if QT_CONFIG(shortcut)
        self.m_actionsave_as.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Shift+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.t_actionprint.setText(
            QCoreApplication.translate("MainWindow", "Print", None)
        )
        # if QT_CONFIG(tooltip)
        self.t_actionprint.setToolTip(
            QCoreApplication.translate("MainWindow", "Print(Ctrl+P)", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.t_actionprint.setStatusTip(
            QCoreApplication.translate("MainWindow", "Print the report ", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.t_actionprint.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.m_actionexit.setText(
            QCoreApplication.translate("MainWindow", "Exit", None)
        )
        # if QT_CONFIG(shortcut)
        self.m_actionexit.setShortcut(
            QCoreApplication.translate("MainWindow", "Esc", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.t_actioncopy.setText(
            QCoreApplication.translate("MainWindow", "Copy ", None)
        )
        # if QT_CONFIG(tooltip)
        self.t_actioncopy.setToolTip(
            QCoreApplication.translate("MainWindow", "Copy(Ctrl+C)", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.t_actioncopy.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Copy selection to clipboard", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.t_actioncopy.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+C", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.t_actionpaste.setText(
            QCoreApplication.translate("MainWindow", "Paste", None)
        )
        # if QT_CONFIG(tooltip)
        self.t_actionpaste.setToolTip(
            QCoreApplication.translate("MainWindow", "Paste(Ctrl+V)", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.t_actionpaste.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Paste the data from clipboard", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.t_actionpaste.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+V", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.m_actiondelete.setText(
            QCoreApplication.translate("MainWindow", "Delete", None)
        )
        # if QT_CONFIG(shortcut)
        self.m_actiondelete.setShortcut(
            QCoreApplication.translate("MainWindow", "Del", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.m_actionnavigation_panel.setText(
            QCoreApplication.translate("MainWindow", "Navigation Panel", None)
        )
        self.m_actionanalysis_panel.setText(
            QCoreApplication.translate("MainWindow", "Analysis Panel", None)
        )
        self.m_actionanalysis_status.setText(
            QCoreApplication.translate("MainWindow", "Analysis Status", None)
        )
        self.m_actionanalysis_parameter.setText(
            QCoreApplication.translate("MainWindow", "Analysis Parameter", None)
        )
        self.m_actionScatter_diagram.setText(
            QCoreApplication.translate("MainWindow", "Scatter Diagram", None)
        )
        self.m_actioncreate_a_pumping_test.setText(
            QCoreApplication.translate("MainWindow", "Create a Pumping Test", None)
        )
        self.m_actioncreate_a_pumping_test_predicition.setText(
            QCoreApplication.translate(
                "MainWindow", "Create a Pumping Test (Predicition)", None
            )
        )
        self.m_actioncreate_new_analysis.setText(
            QCoreApplication.translate("MainWindow", "Create New Analysis", None)
        )
        self.m_actionfit.setText(QCoreApplication.translate("MainWindow", "Fit ", None))
        self.m_actioncomments.setText(
            QCoreApplication.translate("MainWindow", "Comments", None)
        )
        self.actionDuplicate.setText(
            QCoreApplication.translate("MainWindow", "Duplicate", None)
        )
        self.m_actioncontent.setText(
            QCoreApplication.translate("MainWindow", "Content", None)
        )
        self.m_actionweb.setText(
            QCoreApplication.translate("MainWindow", "Web Help...", None)
        )
        self.m_actiontutorial.setText(
            QCoreApplication.translate("MainWindow", "Tutorial...", None)
        )
        self.m_actionabout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.actionRefresh.setText(
            QCoreApplication.translate("MainWindow", "Refresh", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionRefresh.setToolTip(
            QCoreApplication.translate("MainWindow", "Refresh", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.tab_hydro.setTabText(
            self.tab_hydro.indexOf(self.tab_puming_test),
            QCoreApplication.translate("MainWindow", "Pumping Test", None),
        )
        # if QT_CONFIG(tooltip)
        self.tab_hydro.setTabToolTip(
            self.tab_hydro.indexOf(self.tab_puming_test),
            QCoreApplication.translate(
                "MainWindow",
                "Project info , Units . Aquifer proerty , Pumping Test",
                None,
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.tab_hydro.setTabText(
            self.tab_hydro.indexOf(self.tab_pumping_data),
            QCoreApplication.translate("MainWindow", "Pumping Data", None),
        )
        # if QT_CONFIG(tooltip)
        self.tab_hydro.setTabToolTip(
            self.tab_hydro.indexOf(self.tab_pumping_data),
            QCoreApplication.translate(
                "MainWindow", "Drawdown data , discharge , graph", None
            ),
        )
        # endif // QT_CONFIG(tooltip)
        self.tab_hydro.setTabText(
            self.tab_hydro.indexOf(self.tab_analysis),
            QCoreApplication.translate("MainWindow", "Analysis", None),
        )
        # if QT_CONFIG(tooltip)
        self.tab_hydro.setTabToolTip(
            self.tab_hydro.indexOf(self.tab_analysis),
            QCoreApplication.translate("MainWindow", "Solution, Output", None),
        )
        # endif // QT_CONFIG(tooltip)
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", "View", None))
        self.menu_test.setTitle(QCoreApplication.translate("MainWindow", "Test", None))
        self.menu_analysis.setTitle(
            QCoreApplication.translate("MainWindow", "Analysis", None)
        )
        self.menu_tools.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", "toolBar", None)
        )
        # if QT_CONFIG(statustip)
        self.toolBar.setStatusTip("")


# endif // QT_CONFIG(statustip)
# retranslateUi
