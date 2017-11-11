# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from controllers import SerialController

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 472)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../centrale/icons/arduino_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        #####################################################################################################
        self.serial_controller = SerialController()
        #####################################################################################################
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        #####################################################################################################
        self.arduino1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arduino1.sizePolicy().hasHeightForWidth())
        self.arduino1.setSizePolicy(sizePolicy)
        self.arduino1.setStyleSheet("background-color: rgb(201, 211, 211)")
        self.arduino1.setObjectName("arduino1")
        self.verticalLayout.addWidget(self.arduino1)
        #####################################################################################################
        self.arduino2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arduino2.sizePolicy().hasHeightForWidth())
        self.arduino2.setSizePolicy(sizePolicy)
        self.arduino2.setStyleSheet("background-color: rgb(142, 182, 255)")
        self.arduino2.setObjectName("arduino2")
        self.verticalLayout.addWidget(self.arduino2)
        #####################################################################################################
        self.arduino3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arduino3.sizePolicy().hasHeightForWidth())
        self.arduino3.setSizePolicy(sizePolicy)
        self.arduino3.setStyleSheet("background-color: rgb(201, 211, 211)")
        self.arduino3.setObjectName("arduino3")
        self.verticalLayout.addWidget(self.arduino3)
        #####################################################################################################
        self.arduino4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arduino4.sizePolicy().hasHeightForWidth())
        self.arduino4.setSizePolicy(sizePolicy)
        self.arduino4.setStyleSheet("background-color: rgb(201, 211, 211)")
        self.arduino4.setObjectName("arduino4")
        self.verticalLayout.addWidget(self.arduino4)
        #####################################################################################################
        self.arduino5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arduino5.sizePolicy().hasHeightForWidth())
        self.arduino5.setSizePolicy(sizePolicy)
        self.arduino5.setStyleSheet("background-color: rgb(201, 211, 211)")
        self.arduino5.setObjectName("arduino5")
        self.verticalLayout.addWidget(self.arduino5)
        #####################################################################################################
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #####################################################################################################
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.graphs = QtWidgets.QWidget()
        self.graphs.setObjectName("graphs")
        self.stackedWidget = QtWidgets.QStackedWidget(self.graphs)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 20, 331, 261))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        # self.page.addPlot(title="Basic array plotting", y=np.random.normal(size=100)) ################################### LET OP ################################
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.tabWidget.addTab(self.graphs, "")
        #####################################################################################################
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.gridLayout = QtWidgets.QGridLayout(self.settings)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.settings)
        self.label.setWhatsThis("")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.tempscroll_down = QtWidgets.QSlider(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tempscroll_down.sizePolicy().hasHeightForWidth())
        self.tempscroll_down.setSizePolicy(sizePolicy)
        self.tempscroll_down.setMinimum(-40)
        self.tempscroll_down.setMaximum(60)
        self.tempscroll_down.setOrientation(QtCore.Qt.Horizontal)
        self.tempscroll_down.setObjectName("tempscroll_down")
        self.gridLayout.addWidget(self.tempscroll_down, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.settings)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.settings)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lightdown_slider = QtWidgets.QSlider(self.settings)
        self.lightdown_slider.setOrientation(QtCore.Qt.Horizontal)
        self.lightdown_slider.setObjectName("lightdown_slider")
        self.gridLayout.addWidget(self.lightdown_slider, 1, 2, 1, 1)
        self.scrollout_min = QtWidgets.QSlider(self.settings)
        self.scrollout_min.setMinimum(2)
        self.scrollout_min.setMaximum(400)
        self.scrollout_min.setOrientation(QtCore.Qt.Horizontal)
        self.scrollout_min.setObjectName("scrollout_min")
        self.gridLayout.addWidget(self.scrollout_min, 5, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 1, 1, 1)
        self.scrollout_max = QtWidgets.QSlider(self.settings)
        self.scrollout_max.setMinimum(2)
        self.scrollout_max.setMaximum(400)
        self.scrollout_max.setOrientation(QtCore.Qt.Horizontal)
        self.scrollout_max.setObjectName("scrollout_max")
        self.gridLayout.addWidget(self.scrollout_max, 4, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrrollup = QtWidgets.QPushButton(self.settings)
        self.scrrollup.setObjectName("scrrollup")
        self.gridLayout_2.addWidget(self.scrrollup, 1, 0, 1, 1)
        self.scrolldown = QtWidgets.QPushButton(self.settings)
        self.scrolldown.setObjectName("scrolldown")
        self.gridLayout_2.addWidget(self.scrolldown, 1, 1, 1, 1)
        self.lightcheck = QtWidgets.QCheckBox(self.settings)
        self.lightcheck.setObjectName("lightcheck")
        self.gridLayout_2.addWidget(self.lightcheck, 0, 0, 1, 1)
        self.tempcheck = QtWidgets.QCheckBox(self.settings)
        self.tempcheck.setObjectName("tempcheck")
        self.gridLayout_2.addWidget(self.tempcheck, 0, 1, 1, 1)
        self.submit = QtWidgets.QPushButton(self.settings)
        self.submit.setObjectName("submit")
        self.gridLayout_2.addWidget(self.submit, 1, 2, 1, 1)
        self.scrolloutcheck = QtWidgets.QCheckBox(self.settings)
        self.scrolloutcheck.setObjectName("scrolloutcheck")
        self.gridLayout_2.addWidget(self.scrolloutcheck, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 6, 0, 1, 4)
        self.lightup_slider = QtWidgets.QSlider(self.settings)
        self.lightup_slider.setOrientation(QtCore.Qt.Horizontal)
        self.lightup_slider.setObjectName("lightup_slider")
        self.gridLayout.addWidget(self.lightup_slider, 0, 2, 1, 1)
        self.lightup_bar = QtWidgets.QProgressBar(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightup_bar.sizePolicy().hasHeightForWidth())
        self.lightup_bar.setSizePolicy(sizePolicy)
        self.lightup_bar.setProperty("value", 0)
        self.lightup_bar.setObjectName("lightup_bar")
        self.gridLayout.addWidget(self.lightup_bar, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.settings)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 1, 1, 1)
        self.lightdown_bar = QtWidgets.QProgressBar(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightdown_bar.sizePolicy().hasHeightForWidth())
        self.lightdown_bar.setSizePolicy(sizePolicy)
        self.lightdown_bar.setProperty("value", 0)
        self.lightdown_bar.setObjectName("lightdown_bar")
        self.gridLayout.addWidget(self.lightdown_bar, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.tempnumber_up = QtWidgets.QLabel(self.settings)
        self.tempnumber_up.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tempnumber_up.setObjectName("tempnumber_up")
        self.gridLayout.addWidget(self.tempnumber_up, 2, 3, 1, 1)
        self.tempnumber_down = QtWidgets.QLabel(self.settings)
        self.tempnumber_down.setObjectName("tempnumber_down")
        self.gridLayout.addWidget(self.tempnumber_down, 3, 3, 1, 1)
        self.sminout = QtWidgets.QLabel(self.settings)
        self.sminout.setObjectName("sminout")
        self.gridLayout.addWidget(self.sminout, 5, 3, 1, 1)
        self.smaxout = QtWidgets.QLabel(self.settings)
        self.smaxout.setObjectName("smaxout")
        self.gridLayout.addWidget(self.smaxout, 4, 3, 1, 1)
        self.tempscroll_up = QtWidgets.QSlider(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tempscroll_up.sizePolicy().hasHeightForWidth())
        self.tempscroll_up.setSizePolicy(sizePolicy)
        self.tempscroll_up.setMinimum(-40)
        self.tempscroll_up.setMaximum(60)
        self.tempscroll_up.setProperty("value", 0)
        self.tempscroll_up.setOrientation(QtCore.Qt.Horizontal)
        self.tempscroll_up.setObjectName("tempscroll_up")
        self.gridLayout.addWidget(self.tempscroll_up, 2, 2, 1, 1)
        self.tabWidget.addTab(self.settings, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        #####################################################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menubar.setObjectName("menubar")
        #####################################################################################################
        self.menu = QtWidgets.QMenu(self.menubar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("..\centrale\icons\if_menu_2639862.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu.setIcon(icon1)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        #####################################################################################################
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #####################################################################################################
        self.actionClose = QtWidgets.QAction(MainWindow)
        iconquit = QtGui.QIcon()
        iconquit.addPixmap(QtGui.QPixmap("..\centrale\icons\if_minus_2639865.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(iconquit)
        self.actionClose.setObjectName("actionClose")
        #####################################################################################################
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("..\centrale\icons\if_refresh_2639897.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon2)
        self.actionRefresh.setObjectName("actionRefresh")
        #####################################################################################################
        self.menu.addSeparator()
        self.menu.addAction(self.actionRefresh)
        self.menu.addAction(self.actionClose)
        self.menubar.addAction(self.menu.menuAction())
        #####################################################################################################
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        self.lightup_slider.sliderMoved['int'].connect(self.lightup_bar.setValue)
        self.lightdown_slider.sliderMoved['int'].connect(self.lightdown_bar.setValue)
        self.tempscroll_up.sliderMoved['int'].connect(self.tempnumber_up.setNum)
        self.tempscroll_down.sliderMoved['int'].connect(self.tempnumber_down.setNum)
        self.scrollout_max.sliderMoved['int'].connect(self.smaxout.setNum)
        self.scrollout_min.sliderMoved['int'].connect(self.sminout.setNum)
        #####################################################################################################
        self.actionClose.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.actionRefresh.triggered.connect(self.refresh)
        #####################################################################################################
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Central Control"))
        self.arduino1.setText(_translate("MainWindow", "Arduino - Not connected"))
        self.arduino2.setText(_translate("MainWindow", "Arduino - Connected"))
        self.arduino3.setText(_translate("MainWindow", "Arduino - Not connected"))
        self.arduino4.setText(_translate("MainWindow", "Arduino - Not connected"))
        self.arduino5.setText(_translate("MainWindow", "Arduino - Not connected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphs), _translate("MainWindow", "Graphs"))
        self.label_4.setText(_translate("MainWindow", "Scroll up"))
        self.label_7.setText(_translate("MainWindow", "Scroll down"))
        self.label.setText(_translate("MainWindow", "Light"))
        self.label_2.setText(_translate("MainWindow", "Scroll up"))
        self.label_9.setText(_translate("MainWindow", "Scroll out"))
        self.label_8.setText(_translate("MainWindow", "Temperature"))
        self.label_14.setText(_translate("MainWindow", "Min"))
        self.scrrollup.setText(_translate("MainWindow", "Scroll up"))
        self.scrolldown.setText(_translate("MainWindow", "Scroll down"))
        self.lightcheck.setText(_translate("MainWindow", "Light"))
        self.tempcheck.setText(_translate("MainWindow", "Temperature"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.scrolloutcheck.setText(_translate("MainWindow", "Scroll out"))
        self.lightup_bar.setFormat(_translate("MainWindow", "%p%"))
        self.label_13.setText(_translate("MainWindow", "Max"))
        self.label_5.setText(_translate("MainWindow", "Scroll down"))
        self.tempnumber_up.setText(_translate("MainWindow", "0 °C"))
        self.tempnumber_down.setText(_translate("MainWindow", "0 °C"))
        self.sminout.setText(_translate("MainWindow", "2 cm"))
        self.smaxout.setText(_translate("MainWindow", "400 cm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))

    def refresh(self):
        self.serial_controller.connect_ports()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
