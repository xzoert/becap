# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUi.ui'
#
# Created: Fri Jan  6 16:54:54 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 512)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_6 = QtGui.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget_6)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.changeSourceButton = QtGui.QPushButton(self.widget_6)
        self.changeSourceButton.setObjectName("changeSourceButton")
        self.horizontalLayout.addWidget(self.changeSourceButton)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.sourceEdit = QtGui.QLineEdit(self.widget)
        self.sourceEdit.setObjectName("sourceEdit")
        self.verticalLayout_4.addWidget(self.sourceEdit)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtGui.QFrame(self.widget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.widget_8 = QtGui.QWidget(self.widget_2)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.widget_8)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.addExcludeButton = QtGui.QPushButton(self.widget_8)
        self.addExcludeButton.setObjectName("addExcludeButton")
        self.horizontalLayout_3.addWidget(self.addExcludeButton)
        self.verticalLayout.addWidget(self.widget_8)
        self.excludeTableView = QtGui.QTableView(self.widget_2)
        self.excludeTableView.setObjectName("excludeTableView")
        self.excludeTableView.horizontalHeader().setVisible(False)
        self.excludeTableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.excludeTableView)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_7 = QtGui.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.widget_7)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.changeTargetButton = QtGui.QPushButton(self.widget_7)
        self.changeTargetButton.setObjectName("changeTargetButton")
        self.horizontalLayout_2.addWidget(self.changeTargetButton)
        self.verticalLayout_5.addWidget(self.widget_7)
        self.targetEdit = QtGui.QLineEdit(self.widget_3)
        self.targetEdit.setObjectName("targetEdit")
        self.verticalLayout_5.addWidget(self.targetEdit)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.widget_5 = QtGui.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_9 = QtGui.QWidget(self.widget_5)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.backupButton = QtGui.QPushButton(self.widget_9)
        self.backupButton.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.backupButton.setFont(font)
        self.backupButton.setObjectName("backupButton")
        self.horizontalLayout_4.addWidget(self.backupButton)
        self.restoreButton = QtGui.QPushButton(self.widget_9)
        self.restoreButton.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.restoreButton.setFont(font)
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_4.addWidget(self.restoreButton)
        self.verticalLayout_6.addWidget(self.widget_9)
        self.widget_4 = QtGui.QWidget(self.widget_5)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_4 = QtGui.QFrame(self.widget_4)
        self.line_4.setStyleSheet("")
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.statusLabel = QtGui.QLabel(self.widget_4)
        self.statusLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_3.addWidget(self.statusLabel)
        self.statusProgressBar = QtGui.QProgressBar(self.widget_4)
        self.statusProgressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.statusProgressBar.setProperty("value", 24)
        self.statusProgressBar.setObjectName("statusProgressBar")
        self.verticalLayout_3.addWidget(self.statusProgressBar)
        self.verticalLayout_6.addWidget(self.widget_4)
        self.verticalLayout_2.addWidget(self.widget_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Becap", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Source directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.changeSourceButton.setText(QtGui.QApplication.translate("MainWindow", "change", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Directories to exclude:", None, QtGui.QApplication.UnicodeUTF8))
        self.addExcludeButton.setText(QtGui.QApplication.translate("MainWindow", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Target directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.changeTargetButton.setText(QtGui.QApplication.translate("MainWindow", "change", None, QtGui.QApplication.UnicodeUTF8))
        self.backupButton.setText(QtGui.QApplication.translate("MainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreButton.setText(QtGui.QApplication.translate("MainWindow", "Restore", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("MainWindow", "status:", None, QtGui.QApplication.UnicodeUTF8))
