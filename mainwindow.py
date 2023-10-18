# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 445)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(13, 13, 13);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(310, 260, 141, 41))
        self.loginButton.setStyleSheet("QPushButton{\n"
"font: 700 15pt \"Futura\";\n"
"color: rgb(173, 194, 255);\n"
"background-color: rgba(101, 52, 255, 104);\n"
"border-radius:20px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(101, 52, 255, 204);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(22, 22, 61, 189);\n"
"    color: rgb(219, 215, 255);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.signinButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signinButton.setGeometry(QtCore.QRect(390, 220, 111, 21))
        self.signinButton.setStyleSheet("QPushButton{\n"
"font: 700 15pt \"Futura\";\n"
"color: rgb(173, 194, 255);\n"
"    background-color: rgb(51, 68, 95);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(101, 52, 255, 204);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(22, 22, 61, 189);\n"
"    color: rgb(219, 215, 255);\n"
"}")
        self.signinButton.setObjectName("signinButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 210, 151, 41))
        self.label.setStyleSheet("background-color:(0,0,0,0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 70, 261, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    \n"
"border: 1px solid grey;\n"
"border-radius:20px;\n"
"    background-color: rgba(17, 17, 17, 245);\n"
"padding: 10px\n"
"}\n"
"QLineEdit:hover{\n"
"border:1px solid white;\n"
"}\n"
"QLineEdit:pressed{\n"
"border:1px solid rgba(95, 139, 255, 219);\n"
"}\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 150, 261, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    \n"
"border: 1px solid grey;\n"
"border-radius:20px;\n"
"    background-color: rgba(17, 17, 17, 245);\n"
"padding:10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border:1px solid white;\n"
"}\n"
"QLineEdit:pressed{\n"
"border:1px solid rgba(95, 139, 255, 219);\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tryagain = QtWidgets.QLabel(parent=self.centralwidget)
        self.tryagain.setGeometry(QtCore.QRect(220, 310, 321, 20))
        self.tryagain.setText("")
        self.tryagain.setObjectName("tryagain")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Log In"))
        self.signinButton.setText(_translate("MainWindow", "Sign In"))
        self.label.setText(_translate("MainWindow", "do not have an account?"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
