# Form implementation generated from reading ui file 'bin/mainWindow2.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ArchClean(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 346)
        icon = QtGui.QIcon.fromTheme("delete")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setResizeMode(QtWidgets.QListView.ResizeMode.Adjust)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_settings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_settings.setStyleSheet("font: 11pt \"Comfortaa\";")
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.horizontalLayout.addWidget(self.pushButton_settings)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_abort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_abort.setStyleSheet("font: 11pt \"Comfortaa\";")
        self.pushButton_abort.setObjectName("pushButton_abort")
        self.horizontalLayout.addWidget(self.pushButton_abort)
        self.pushButton_start = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_start.setStyleSheet("font: 11pt \"Comfortaa\";")
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_settings.setText(_translate("MainWindow", "Settings"))
        self.pushButton_abort.setText(_translate("MainWindow", "Exit"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))